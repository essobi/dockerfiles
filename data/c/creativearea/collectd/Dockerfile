FROM ubuntu:14.04  
MAINTAINER CREATIVE AREA  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV COLLECTD_VERSION 5.5.0  
ENV COLLECTD_PATH /opt/collectd  
ENV LOGSTASH_SERVER logstash  
ENV LOGSTASH_PORT 25826  
ADD http://collectd.org/files/collectd-${COLLECTD_VERSION}.tar.gz /tmp/  
  
RUN apt-get update && apt-get install -yq --no-install-recommends build-
essential libcurl4-openssl-dev git python-dev python-pip  
  
RUN cd /tmp && \  
tar xzf collectd-${COLLECTD_VERSION}.tar.gz && \  
cd collectd-${COLLECTD_VERSION} && \  
./configure --prefix=${COLLECTD_PATH} \--disable-all-plugins --enable-network
--enable-python && \  
make && \  
make install  
  
RUN git clone https://github.com/lebauce/docker-collectd-plugin.git
${COLLECTD_PATH}/share/docker-collectd-plugin && \  
pip install -r ${COLLECTD_PATH}/share/docker-collectd-plugin/requirements.txt  
  
RUN rm -rf /tmp/collectd-${COLLECTD_VERSION} && \  
apt-get remove --purge -y build-essential git libcurl4-openssl-dev python-dev
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY collectd.conf ${COLLECTD_PATH}/etc/collectd.conf  
  
COPY start.sh /collectd_start.sh  
RUN chmod a+x /collectd_start.sh  
  
CMD /collectd_start.sh  

