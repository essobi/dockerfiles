FROM openjdk:8-alpine  
  
MAINTAINER Jaroslav Kostal <jaroslav@kostal.sk>  
  
ARG GLOWROOT_VERSION="0.10.0"  
RUN wget
"https://github.com/glowroot/glowroot/releases/download/v${GLOWROOT_VERSION}/glowroot-
central-${GLOWROOT_VERSION}-dist.zip" -P / -O /glowroot-central-dist.zip;\  
unzip /glowroot-central-dist.zip;\  
rm /glowroot-central-dist.zip  
  
WORKDIR /glowroot-central  
  
RUN mkdir config;\  
mv glowroot-central.properties glowroot-central.properties.default;\  
ln -s config/glowroot-central.properties glowroot-central.properties  
  
COPY entrypoint.sh .  
  
VOLUME /glowroot-central/config  
  
EXPOSE 4000 8181  
ENV CASSANDRA_HOST="cassandra"  
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]  

