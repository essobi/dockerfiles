FROM ubuntu:16.04  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install default-jre-headless wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN cd /opt && \  
wget -q https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz &&
\  
mkdir /opt/spark && \  
tar -xzvf spark-2.2.0-bin-hadoop2.7.tgz -C /opt/spark --strip-components=1 &&
\  
rm spark-2.2.0-bin-hadoop2.7.tgz  
ADD ./ /opt/  
EXPOSE 8080  
EXPOSE 8081  
EXPOSE 7077  
EXPOSE 6066  
ENTRYPOINT ["/opt/docker_entrypoint.sh"]  

