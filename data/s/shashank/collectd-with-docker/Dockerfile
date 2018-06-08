# based on fr3nd/docker-collectd/Dockerfile  
FROM ubuntu:vivid  
  
MAINTAINER shashank  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
python-dev \  
librdkafka-dev \  
zlib1g-dev \  
python-pip \  
wget \  
git && \  
rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
#ENV COLLECTD_VERSION collectd-5.5.0  
WORKDIR /opt  
RUN wget https://collectd.org/files/collectd-5.5.0.tar.bz2  
RUN tar xvf collectd-5.5.0.tar.bz2  
WORKDIR /opt/collectd-5.5.0  
  
RUN ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc/collectd \  
\--without-libstatgrab \  
\--without-included-ltdl \  
\--disable-static  
RUN make all  
RUN make install  
RUN make clean  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
#using lebauce/docker-collectd-plugin  
WORKDIR /opt  
RUN git clone https://github.com/lebauce/docker-collectd-plugin.git  
RUN pip install -r /opt/docker-collectd-plugin/requirements.txt  
  
ADD collectd.conf /etc/collectd/  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

