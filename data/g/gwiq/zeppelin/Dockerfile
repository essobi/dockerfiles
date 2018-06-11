FROM gwiq/spark  
MAINTAINER Jakub Liska <liska.jakub@gmail.com>  
  
ENV PATH .:$PATH  
  
RUN apt-get update -y && \  
apt-get install -y git net-tools build-essential npm inotify-tools
libfontconfig python python-setuptools python-dev python-numpy python-pip
python-matplotlib ipython python-pandas python-nose && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade awscli  
RUN easy_install py4j pattern pandasql numpy sympy  
  
# Install Tini  
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.6.0/tini
&& \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
ENV MAVEN_VERSION 3.3.1  
RUN curl -sL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | gunzip | tar x -C /opt/  
  
ENV ZEPPELIN_REPO_URL https://github.com/apache/incubator-zeppelin.git  
ENV ZEPPELIN_REPO_BRANCH master  
ENV ZEPPELIN_HOME /opt/zeppelin  
ENV ZEPPELIN_CONF_DIR $ZEPPELIN_HOME/conf  
ENV ZEPPELIN_NOTEBOOK_DIR $ZEPPELIN_HOME/notebook  
ENV ZEPPELIN_PORT 8080  
ENV SCALA_BINARY_VERSION 2.10  
ENV SCALA_VERSION $SCALA_BINARY_VERSION.4  
ENV SPARK_PROFILE 1.5  
ENV SPARK_VERSION 1.5.1  
ENV HADOOP_PROFILE 2.6  
ENV HADOOP_VERSION 2.6.2  
### ZEPPELIN ###  
WORKDIR /opt  
  
ENV PATH $ZEPPELIN_HOME/zeppelin-web/node:$PATH  
ENV PATH $ZEPPELIN_HOME/zeppelin-web/node_modules/grunt-cli/bin:$PATH  
  
RUN git config --global url."https://".insteadOf git://  
  
RUN git clone $ZEPPELIN_REPO_URL $ZEPPELIN_HOME  
  
WORKDIR $ZEPPELIN_HOME  
  
RUN git checkout $ZEPPELIN_REPO_BRANCH  
  
RUN /opt/apache-maven-${MAVEN_VERSION}/bin/mvn clean \  
install \  
-pl '!flink,!ignite,!phoenix,!postgresql,!tajo,!hive,!cassandra,!lens,!kylin' \  
-Phadoop-$HADOOP_PROFILE \  
-Dhadoop.version=$HADOOP_VERSION \  
-Pspark-$SPARK_PROFILE \  
-Dspark.version=$SPARK_VERSION \  
-Ppyspark \  
-Dscala.version=$SCALA_VERSION \  
-Dscala.binary.version=$SCALA_BINARY_VERSION \  
-Dmaven.findbugs.enable=false \  
-Drat.skip=true \  
-Dcheckstyle.skip=true \  
-DskipTests \  
"$@"  
  
ENV PATH $ZEPPELIN_HOME/bin:$PATH  
  
RUN mkdir /opt/zeppelin/logs  
RUN mkdir /opt/zeppelin/run  
  
### CLEAN ###  
RUN rm -rf /root/.m2  
RUN rm -rf /root/.npm  
  
COPY start-notebook.sh /usr/local/bin/  
  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]

