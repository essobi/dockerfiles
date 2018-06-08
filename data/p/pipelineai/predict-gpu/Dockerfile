FROM pipelineai/tensorflow-serving-gpu:1.5.0  
WORKDIR /root  
  
ENV \  
TERM=xterm  
  
###################  
# Setup OpenJDK 1.8  
###################  
RUN \  
apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends openjdk-8-jdk openjdk-8-jre-
headless \  
&& apt-get install -y apt-transport-https \  
&& apt-get install -y wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV \  
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/  
  
ENV \  
SHELL=/bin/bash  
  
RUN \  
rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
RUN \  
echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated sbt=1.0.2  
  
# Install Anaconda with Python3  
RUN wget -q
https://repo.continuum.io/miniconda/Miniconda3-4.3.31-Linux-x86_64.sh -O
/tmp/miniconda.sh && \  
echo '7fe70b214bee1143e3e3f0467b71453c */tmp/miniconda.sh' | md5sum -c - && \  
bash /tmp/miniconda.sh -f -b -p /opt/conda && \  
/opt/conda/bin/conda install --yes python=3.6 sqlalchemy tornado jinja2
traitlets requests pip && \  
/opt/conda/bin/pip install --upgrade pip && \  
rm /tmp/miniconda.sh  
  
ENV \  
PATH=/opt/conda/bin:$PATH  
  
#RUN \  
# conda update -n base conda  
RUN \  
pip install --upgrade pip  
  
COPY config/prometheus/ config/prometheus/  
ENV \  
PROMETHEUS_VERSION=2.0.0  
RUN \  
wget
https://github.com/prometheus/prometheus/releases/download/v$PROMETHEUS_VERSION/prometheus-$PROMETHEUS_VERSION.linux-
amd64.tar.gz \  
&& tar xvfz prometheus-$PROMETHEUS_VERSION.linux-amd64.tar.gz \  
&& rm prometheus-$PROMETHEUS_VERSION.linux-amd64.tar.gz  
  
RUN \  
mv /root/prometheus-$PROMETHEUS_VERSION.linux-amd64/prometheus.yml
/root/prometheus-$PROMETHEUS_VERSION.linux-amd64/prometheus.yml.orig \  
&& cd /root/prometheus-$PROMETHEUS_VERSION.linux-amd64/ \  
&& ln -s /root/config/prometheus/prometheus.yml  
  
ENV \  
PATH=/root/prometheus-$PROMETHEUS_VERSION.linux-amd64/:$PATH  
  
COPY config/grafana/ config/grafana/  
ENV \  
GRAFANA_VERSION=4.6.3  
RUN \  
wget https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana-$GRAFANA_VERSION.linux-x64.tar.gz \  
&& tar -zxvf grafana-$GRAFANA_VERSION.linux-x64.tar.gz \  
&& rm grafana-$GRAFANA_VERSION.linux-x64.tar.gz  
  
ENV \  
PATH=/root/grafana-$GRAFANA_VERSION/bin:$PATH  
  
RUN \  
cd /root/grafana-$GRAFANA_VERSION/conf \  
&& ln -s /root/config/grafana/custom.ini \  
&& ln -s /root/config/grafana/dashboards  
  
RUN \  
mkdir -p /root/logs  
  
ENV \  
LOGS_HOME=/root/logs  
  
COPY sysutils/ sysutils/  
COPY jvm/ jvm/  
  
ENV \  
PIPELINE_JVM_MODEL_SERVER_PATH=/root/jvm  
  
RUN \  
cd $PIPELINE_JVM_MODEL_SERVER_PATH \  
&& ./build.sh  
  
ENV \  
CONFLUENT_VERSION=4.0.0 \  
CONFLUENT_MAJOR_VERSION=4.0  
ENV \  
CONFLUENT_HOME=/root/confluent-${CONFLUENT_VERSION}  
  
ENV \  
PATH=$CONFLUENT_HOME/bin:$PATH  
  
RUN \  
wget
http://packages.confluent.io/archive/${CONFLUENT_MAJOR_VERSION}/confluent-
oss-${CONFLUENT_VERSION}-2.11.tar.gz \  
&& tar xvzf confluent-oss-${CONFLUENT_VERSION}-2.11.tar.gz \  
&& rm confluent-oss-${CONFLUENT_VERSION}-2.11.tar.gz  
  
RUN \  
git clone https://github.com/edenhill/librdkafka.git \  
&& cd librdkafka \  
&& ./configure \  
&& make \  
&& make install  
  
RUN \  
pip install git+https://github.com/wintoncode/winton-kafka-streams.git  
  
RUN \  
apt-get install -y nginx  
  
RUN \  
service nginx start  
  
COPY config/nginx/ config/nginx/  
  
RUN \  
mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.orig
\  
&& cd /etc/nginx/sites-available/ \  
&& ln -s /root/config/nginx/default \  
&& cd /etc/nginx/sites-enabled/ \  
&& rm default \  
&& ln -s /etc/nginx/sites-available/default  
  
#ENV \  
# PIPELINE_WEBSOCKET_KAFKA_SERVER_PATH=/root/src/main/python/kafka  
#ENV \  
# PIPELINE_WEBSOCKET_KAFKA_SERVER_PORT=5959  
#ENV \  
# PIPELINE_WEBSOCKET_KAFKA_SERVER_UPDATE_INTERVAL=1000  
#ENV \  
# PIPELINE_WEBSOCKET_KAFKA_CONDA_ENV_NAME=pipeline-websocket-kafka  
# Must run ths or you will see the following error:  
# ImportError: librdkafka.so.1: cannot open shared object file: No such file
or directory  
RUN \  
ldconfig  
  
ENV \  
PIPELINE_MODEL_SERVER_PATH=/root/src/main/python/model_server  
  
ENV \  
PIPELINE_MODEL_SERVER_PORT=9876  
ENV \  
PIPELINE_MODEL_SERVER_PROMETHEUS_PORT=10254  
ENV \  
PIPELINE_MODEL_SERVER_TENSORFLOW_SERVING_PORT=9000  
ENV \  
PIPELINE_MODEL_SERVER_TENSORFLOW_SERVING_REQUEST_BATCHING=true  
  
#RUN \  
# echo "" \  
# && echo "Installing TensorFlow Serving..." \  
# && echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-
apt stable tensorflow-model-server tensorflow-model-server-universal" | tee
/etc/apt/sources.list.d/tensorflow-serving.list \  
# && curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-
serving.release.pub.gpg | apt-key add - \  
# && apt-get update \  
# && apt-get install -y tensorflow-model-server;  
ENV \  
PIPELINE_HYSTRIX_DASHBOARD_PORT=7979  
COPY dashboard/jetty-0.4.7.RC0.jar dashboard/jetty-0.4.7.RC0.jar  
COPY dashboard/hystrix-dashboard-0.1.0-dev.0.uncommitted.war
dashboard/hystrix-dashboard-0.1.0-dev.0.uncommitted.war  
COPY html/ /var/www/html/  
COPY run run  
COPY src/ src/  
COPY config/kafka/ config/kafka/  
  
RUN \  
apt-get install -y vim  
  
#RUN \  
# echo "Installing Caffe..." \  
# && echo "deb http://ftp2.cn.debian.org/debian sid main contrib non-free" |
tee /etc/apt/sources.list.d/caffe2.list \  
# && apt-get install -y caffe-cuda  
ENV \  
LD_LIBRARY_PATH=/usr/lib/x86_64-linux-
gnu:/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
  
# Don't forget to update the pipeline cli if these ports change!  
EXPOSE \  
# Nginx (80 is too common and could clash with local development) \  
8080 \  
# Python-based Model Server (Primary Model) \  
# 9876 \  
# TensorFlow-based Model Server (Primary Model) \  
# 9000 \  
# JVM-based Model Server (Primary Model) \  
# 9040 \  
# Prometheus Metrics Server \  
9090 \  
# Grafana Dashboards \  
3000  
# Kafka Broker \  
# 9092 \  
# Kafka REST API \  
# 8082 \  
# Kafka Schema Manager \  
# 8081 \  
# ZooKeeper \  
# 2181 \  
# WebSocket-based Kafka Consumer \  
# 5959 \  
# TensorBoard \  
# 6006 \  
# TensorFlow Training UI (Guild) \  
# 6333 \  
# Hystrix Dashboard \  
# 7979 \  
# Prometheus Endpoint (Python)  
# 10254  
# Executes the ./run script upon startup  
ENTRYPOINT ["./run"]  

