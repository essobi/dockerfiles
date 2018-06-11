FROM ubuntu:14.04  
MAINTAINER Andreas Lang <andreas.lang@aquilainsight.com>  
  
ENV TERM=xterm \  
MIRROR=http://mirrors.ukfast.co.uk/sites/ftp.apache.org/  
ENV ZEPPELIN_VERSION=0.6.0 \  
ZEPPELIN_SRV_DIR=/srv/zeppelin  
ENV ZEPPELIN_ARCHIVE=zeppelin-$ZEPPELIN_VERSION-bin-all  
ENV ZEPPELIN_HOME=/opt/zeppelin/$ZEPPELIN_ARCHIVE \  
ZEPPELIN_NOTEBOOK_DIR=$ZEPPELIN_SRV_DIR/notebooks  
  
RUN apt-get update && apt-get install -y \  
curl \  
openjdk-7-jdk \  
python-numpy \  
python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install httpagentparser  
  
RUN mkdir /opt/zeppelin  
WORKDIR /opt/zeppelin  
RUN curl $MIRROR/zeppelin/zeppelin-${ZEPPELIN_VERSION}/${ZEPPELIN_ARCHIVE}.tgz
| tar xfz -  
  
COPY lib/*.jar ${ZEPPELIN_HOME}/lib/  
  
EXPOSE 8080  
ENV PATH=$PATH:$ZEPPELIN_HOME/bin  
RUN mkdir -p $ZEPPELIN_NOTEBOOK_DIR  
  
WORKDIR $ZEPPELIN_SRV_DIR  
ADD run.sh run.sh  
  
CMD $ZEPPELIN_SRV_DIR/run.sh  

