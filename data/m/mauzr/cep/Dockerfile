FROM alpine:edge  
  
RUN apk add --no-cache openjdk8-jre  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL \  
org.label-schema.schema-version=1.0 \  
org.label-schema.name=mauzr/cep \  
org.label-schema.vcs-url=https://github.com/mauzr/cep \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version=$VERSION \  
net.eqrx.mauzr.cep.version=$VERSION \  
net.eqrx.mauzr.cep.vcs-ref=$VCS_REF  
  
COPY . /opt/cep  
WORKDIR /opt/cep  
  
RUN apk add --no-cache openjdk8 maven && mvn clean compile assembly:single &&
\  
mv target/cep-1-jar-with-dependencies.jar cep.jar && apk \  
del openjdk8 maven && rm -rf /root/.m2  

