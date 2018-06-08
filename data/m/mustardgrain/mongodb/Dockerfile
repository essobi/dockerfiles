FROM mustardgrain/base:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV MONGODB_VERSION 2.6.0  
ENV MONGODB_LONG_VERSION linux-x86_64-$MONGODB_VERSION  
ENV MONGODB_URL
http://downloads.mongodb.org/linux/mongodb-$MONGODB_LONG_VERSION.tgz  
ENV MONGODB_HOME /opt/mongodb-$MONGODB_LONG_VERSION  
  
RUN cd /opt && /usr/bin/curl -L -s $MONGODB_URL | tar xz  
  
COPY . /src  
  
RUN mkdir -p /etc/service/mongodb && cp /src/run /etc/service/mongodb  
  
WORKDIR $MONGODB_HOME  
  
EXPOSE 27017  
EXPOSE 28017  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

