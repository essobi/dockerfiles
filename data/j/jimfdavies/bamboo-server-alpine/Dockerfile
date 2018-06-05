# Bamboo Server  
# With thanks to https://github.com/hwuethrich/docker-images  
FROM openjdk:alpine  
  
ENV BAMBOO_VERSION 6.1.1  
ENV BAMBOO_HOME /home/bamboo  
  
EXPOSE 8085 54663  
COPY bamboo-server.sh /bamboo-server.sh  
  
RUN \  
apk add --update \  
ca-certificates \  
wget \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/bamboo-server.sh"]  

