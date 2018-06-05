FROM java:8-alpine  
MAINTAINER He Bai <bai.he@outlook.com>  
  
WORKDIR /root  
  
# Environment variables of package versions  
ENV HADOOP_VERSION 2.5.2  
ENV HIVE_VERSION 1.2.1  
ENV MYSQL_JDBC_VERSION 5.1.38  
ENV PG_JDBC_VERSION 9.4.1208  
ENV SPARK_VERSION 1.6.1-bin-hadoop2.4  
ENV STRATIO_VERSION 0.11.1  
ENV SCALA_VERSION 2.10  
ENV CASBAH_VERSION 3.1.1  
ENV MONGO_HADOOP_VERSION 1.5.2  
ENV MONGO_DRIVER_VERSION 3.2.2  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# gpg: key F73C700D: public key "Larry Hastings <larry@hastings.org>" imported  
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D  
  
ENV PYTHON_VERSION 3.5.1  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 8.1.2  
# Environment variables of hadoop / hive / spark directories  
ENV HADOOP_DIR hadoop-${HADOOP_VERSION}  
ENV HIVE_DIR apache-hive-${HIVE_VERSION}-bin  
ENV SPARK_DIR spark-${SPARK_VERSION}  
ENV SPARK_HOME /root/${SPARK_DIR}  
  
# The external jars  
ENV EXT_LIB_DIR extlibs  
ENV NOTEBOOK_DIR notebook  
  
# Add required jars into a extra libarary directory  
RUN mkdir ${EXT_LIB_DIR}  
# Mysql JDBC driver  
ADD http://repo1.maven.org/maven2/mysql/mysql-connector-
java/${MYSQL_JDBC_VERSION}/mysql-connector-java-${MYSQL_JDBC_VERSION}.jar
/root/${EXT_LIB_DIR}  
# PostgreSQL JDBC driver  
ADD https://jdbc.postgresql.org/download/postgresql-${PG_JDBC_VERSION}.jar
/root/${EXT_LIB_DIR}  
# Mongo-Stratio dependendies  
ADD http://repo1.maven.org/maven2/org/mongodb/casbah-
commons_${SCALA_VERSION}/${CASBAH_VERSION}/casbah-
commons_${SCALA_VERSION}-${CASBAH_VERSION}.jar /root/${EXT_LIB_DIR}  
ADD http://repo1.maven.org/maven2/org/mongodb/casbah-
core_${SCALA_VERSION}/${CASBAH_VERSION}/casbah-
core_${SCALA_VERSION}-${CASBAH_VERSION}.jar /root/${EXT_LIB_DIR}  
ADD http://repo1.maven.org/maven2/org/mongodb/casbah-
query_${SCALA_VERSION}/${CASBAH_VERSION}/casbah-
query_${SCALA_VERSION}-${CASBAH_VERSION}.jar /root/${EXT_LIB_DIR}  
ADD http://repo1.maven.org/maven2/com/stratio/datasource/spark-
mongodb_${SCALA_VERSION}/${STRATIO_VERSION}/spark-
mongodb_${SCALA_VERSION}-${STRATIO_VERSION}.jar /root/${EXT_LIB_DIR}  
ADD http://repo1.maven.org/maven2/org/mongodb/mongo-hadoop/mongo-hadoop-
core/${MONGO_HADOOP_VERSION}/mongo-hadoop-core-${MONGO_HADOOP_VERSION}.jar
/root/${EXT_LIB_DIR}  
ADD http://repo1.maven.org/maven2/org/mongodb/mongo-java-
driver/${MONGO_DRIVER_VERSION}/mongo-java-driver-${MONGO_DRIVER_VERSION}.jar
/root/${EXT_LIB_DIR}  
  
# add python requirements  
ADD requirements.txt /root/requirements.txt  
  
# Install python related packages  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps curl gnupg \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -r "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src \  
&& tar -xJC /usr/src -f python.tar.xz \  
&& mv "/usr/src/Python-$PYTHON_VERSION" /usr/src/python \  
&& rm python.tar.xz \  
&& apk del .fetch-deps \  
\  
&& apk add --no-cache --virtual .build-deps \  
bzip2-dev \  
g++ \  
libc-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl-dev \  
pax-utils \  
readline-dev \  
sqlite-dev \  
xz-dev \  
zlib-dev \  
postgresql-dev \  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& pip3 install --no-cache-dir --upgrade --ignore-installed
pip==$PYTHON_PIP_VERSION \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip3 install -r /root/requirements.txt \  
&& pip3 install jupyter \  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .python-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/python ~/.cache  
  
# make some useful symlinks that are expected to exist  
#RUN cd /usr/local/bin \  
# && ln -s easy_install-3.5 easy_install \  
# && ln -s idle3 idle \  
# && ln -s pydoc3 pydoc \  
# && ln -s python3 python \  
# && ln -s python3-config python-config  
# Install hadoop, hive and spark  
ADD http://www-
us.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
/root  
ADD http://www-us.apache.org/dist/hive/hive-${HIVE_VERSION}/apache-
hive-${HIVE_VERSION}-bin.tar.gz /root  
ADD http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}.tgz /root  
  
RUN cd /root && tar xvzf hadoop-${HADOOP_VERSION}.tar.gz \  
&& tar xvzf apache-hive-${HIVE_VERSION}-bin.tar.gz \  
&& tar xvzf spark-${SPARK_VERSION}.tgz \  
&& rm hadoop-${HADOOP_VERSION}.tar.gz apache-hive-${HIVE_VERSION}-bin.tar.gz
spark-${SPARK_VERSION}.tgz  
  
# Add Mysql JDBC driver to hive lib-path  
RUN cp /root/${EXT_LIB_DIR}/mysql-connector-java-${MYSQL_JDBC_VERSION}.jar
${HIVE_DIR}/lib/mysql-connector-java-${MYSQL_JDBC_VERSION}-bin.jar  
  
# Place hive-site to Hive & Spark  
ADD hive-site.xml /root/${HIVE_DIR}/conf/hive-site.xml  
ADD hive-site.xml /root/${SPARK_DIR}/conf/hive-site.xml  
  
# Install the jupyter notebook  
RUN mkdir -p /root/${NOTEBOOK_DIR}  
#ADD spark.ipynb /root/${NOTEBOOK_DIR}  
# Add entry scripts  
ADD start-hive-metastore.sh /root/start-hive-metastore.sh  
RUN chmod +x /root/start-hive-metastore.sh  
  
ADD start-sparksql-thrift.sh /root/start-sparksql-thrift.sh  
RUN chmod +x /root/start-sparksql-thrift.sh  
  
ADD start-jupyter-notebook.sh /root/start-jupyter-notebook.sh  
RUN chmod +x /root/start-jupyter-notebook.sh  
  

