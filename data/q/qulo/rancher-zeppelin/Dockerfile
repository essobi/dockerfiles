FROM qulo/spark:2.1.1-hadoop-2.8  
# SciPy  
RUN set -ex \  
&& buildDeps=' \  
libpython3-dev \  
build-essential \  
pkg-config \  
gfortran \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends \  
$buildDeps \  
ca-certificates \  
wget \  
r-base \  
liblapack-dev \  
libopenblas-dev \  
&& packages=' \  
numpy \  
pandasql \  
scipy \  
' \  
&& pip3 install $packages \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Zeppelin  
ENV ZEPPELIN_PORT 8080  
ENV ZEPPELIN_HOME /usr/zeppelin  
ENV ZEPPELIN_CONF_DIR $ZEPPELIN_HOME/conf  
ENV ZEPPELIN_NOTEBOOK_DIR $ZEPPELIN_HOME/notebook  
ENV ZEPPELIN_COMMIT v0.7.2  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN set -ex \  
&& buildDeps=' \  
git \  
bzip2 \  
npm \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps \  
&& curl -sL
http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
| gunzip \  
| tar x -C /tmp/ \  
&& git clone https://github.com/apache/zeppelin.git /usr/src/zeppelin \  
&& cd /usr/src/zeppelin \  
&& git checkout -q $ZEPPELIN_COMMIT \  
&& dev/change_scala_version.sh "2.11" \  
&& MAVEN_OPTS="-Xmx2g -XX:MaxPermSize=1024m" /tmp/apache-maven-3.3.9/bin/mvn
--batch-mode package -DskipTests -Pscala-2.11 -Pbuild-distr \  
-pl 'zeppelin-interpreter,zeppelin-zengine,zeppelin-display,spark-dependencies,spark,markdown,angular,shell,hbase,postgresql,jdbc,python,elasticsearch,zeppelin-web,zeppelin-server,zeppelin-distribution' \  
&& tar xvf /usr/src/zeppelin/zeppelin-distribution/target/zeppelin*.tar.gz -C
/usr/ \  
&& mv /usr/zeppelin* $ZEPPELIN_HOME \  
&& mkdir -p $ZEPPELIN_HOME/logs \  
&& mkdir -p $ZEPPELIN_HOME/run \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/src/zeppelin \  
&& rm -rf /root/.m2 \  
&& rm -rf /root/.npm \  
&& rm -rf /tmp/*  
  
#gcloud  
RUN apt-get update && \  
apt-get install -y lsb-release apt-transport-https && \  
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && \  
apt-get install -y google-cloud-sdk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install cement && \  
pip install boto3 && \  
pip install sqlparse && \  
pip install plotly && \  
pip install httplib2 && \  
pip install termcolor && \  
pip install awscli && \  
pip install --upgrade google-api-python-client  
  
ADD about.json $ZEPPELIN_NOTEBOOK_DIR/2BTRWA9EV/note.json  
WORKDIR $ZEPPELIN_HOME  
ADD entrypoint.sh .  
  
CMD ["entrypoint.sh"]  

