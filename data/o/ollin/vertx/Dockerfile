FROM java:8  
MAINTAINER Oliver Nautsch <oliver.nautsch@gmail.com>  
  
RUN wget http://dl.bintray.com/vertx/downloads/vert.x-2.1.5.tar.gz && \  
tar zxf vert.x-2.1.5.tar.gz -C /usr/share && \  
rm vert.x-2.1.5.tar.gz && \  
ln -s /usr/share/vert.x-2.1.5/bin/vertx /usr/bin/vertx  
  
CMD ["vertx"]  
  

