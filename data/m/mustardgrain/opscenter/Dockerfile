FROM mustardgrain/python:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV OPSCENTER_VERSION 5.2.0  
ENV OPSCENTER_URL
http://downloads.datastax.com/community/opscenter-$OPSCENTER_VERSION.tar.gz  
ENV OPSCENTER_HOME /opt/opscenter-$OPSCENTER_VERSION  
  
RUN cd /opt && /usr/bin/curl -L -s $OPSCENTER_URL | tar xz  
  
COPY . /src  
  
RUN mkdir -p /etc/service/opscenter && cp /src/run /etc/service/opscenter  
  
WORKDIR $OPSCENTER_HOME  
  
EXPOSE 8888  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

