FROM openjdk:8u102-jdk  
  
RUN apt-get install wget \  
&& wget
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz  
  
COPY rhizome.yaml /opt  
COPY rhizome.yaml.prod /opt  
  
ARG IMAGE_NAME  
ARG IMG_VER  
ARG ENV  
ENV VERSION=${IMG_VER:-v1.0.0} NAME=${IMAGE_NAME:-derpName} TARGET=${ENV}  
  
ADD $NAME.tgz /opt  
  
RUN cd /opt/$NAME/lib \  
&& mv /opt/rhizome.yaml$TARGET ./rhizome.yaml \  
&& jar vfu $NAME-$VERSION.jar rhizome.yaml \  
&& rm /opt/rhizome.yaml*  
  
EXPOSE 8080  
CMD dockerize -wait tcp://conductor:5701 -timeout 300s; /opt/$NAME/bin/$NAME
cassandra  

