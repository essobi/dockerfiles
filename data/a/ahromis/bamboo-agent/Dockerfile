FROM java:7u75-jre  
MAINTAINER Andrew Hromis "http://hromis.com"  
RUN apt-get update && apt-get install -y wget git && rm -rf
/var/lib/apt/lists/*  
ADD https://get.docker.io/builds/Linux/x86_64/docker-latest
/usr/local/bin/docker  
RUN chmod +x /usr/local/bin/docker  
COPY start.sh /usr/local/bin/start.sh  
  
ENV BAMBOO_HOME /data/bamboo-agent-home  
  
CMD ["/usr/local/bin/start.sh"]  

