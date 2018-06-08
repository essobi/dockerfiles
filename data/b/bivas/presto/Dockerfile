FROM openjdk:8-jre-slim  
  
ARG MIRROR="https://repo1.maven.org/maven2/com/facebook/presto"  
ARG PRESTO_VERSION="0.198"  
ARG PRESTO_BIN="${MIRROR}/presto-server/${PRESTO_VERSION}/presto-
server-${PRESTO_VERSION}.tar.gz"  
ARG PRESTO_CLI_BIN="${MIRROR}/presto-cli/${PRESTO_VERSION}/presto-
cli-${PRESTO_VERSION}-executable.jar"  
USER root  
  
RUN apt-get update && \  
apt-get install -y --allow-unauthenticated curl wget less && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV PRESTO_HOME /presto  
ENV PRESTO_USER presto  
ENV PRESTO_CONF_DIR ${PRESTO_HOME}/etc  
ENV PATH $PATH:$PRESTO_HOME/bin  
  
RUN useradd \  
\--create-home \  
\--home-dir ${PRESTO_HOME} \  
\--shell /bin/bash \  
$PRESTO_USER  
  
RUN mkdir -p $PRESTO_HOME && \  
wget --quiet $PRESTO_BIN && \  
tar xzf presto-server-${PRESTO_VERSION}.tar.gz && \  
rm -rf presto-server-${PRESTO_VERSION}.tar.gz && \  
mv presto-server-${PRESTO_VERSION}/* $PRESTO_HOME && \  
rm -rf presto-server-${PRESTO_VERSION} && \  
mkdir -p ${PRESTO_CONF_DIR}/catalog/ && \  
mkdir -p ${PRESTO_HOME}/data && \  
cd ${PRESTO_HOME}/bin && \  
wget --quiet ${PRESTO_CLI_BIN} && \  
mv presto-cli-${PRESTO_VERSION}-executable.jar presto && \  
chmod +x presto && \  
chown -R ${PRESTO_USER}:${PRESTO_USER} $PRESTO_HOME  
  
# Need to work with python2  
# See: https://github.com/prestodb/presto/issues/4678  
ENV PYTHON2_DEBIAN_VERSION 2.7.13-2  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python="${PYTHON2_DEBIAN_VERSION}" \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /usr/local/bin \  
&& rm -rf idle pydoc python python-config  
  
USER $PRESTO_USER  
  
CMD ["launcher", "run"]  

