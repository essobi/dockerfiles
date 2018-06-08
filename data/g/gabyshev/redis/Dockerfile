FROM redis:3.2.9  
ENV DOCKERIZE_VERSION v0.4.0  
RUN apt-get update && apt-get install -y wget \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY bin/run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
COPY config/ /redis/config  
  
#GENERAL  
# ENV ANNOUNCE_IP # Required variable  
ENV REDIS_PORT 6379  
# ENV CONFIGS # Not required field in format
variable1=value1[;variable2=value2[;...]]  
#SENTINEL  
ENV MASTER_NAME mymaster  
# ENV MASTER_IP 127.0.0.1 #Required field  
ENV QUORUM 2  
ENV SENTINEL_PORT 26379  
ENV MASTER_PORT 6379  
#SLAVES  
# ENV MASTER_ADDRESS # Required variable  
CMD ["/usr/local/bin/run.sh"]

