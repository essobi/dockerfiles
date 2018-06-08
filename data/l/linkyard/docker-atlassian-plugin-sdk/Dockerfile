FROM openjdk:8u141  
MAINTAINER Mario Siegenthaler <mario.siegenthaler@linkyard.ch>  
  
# Install the plugin SDK  
RUN apt-get update && \  
apt-get install -y apt-transport-https && \  
echo "deb https://sdkrepo.atlassian.com/debian/ stable contrib" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
B07804338C015B73 && \  
apt-get update && \  
apt-get install -y atlassian-plugin-sdk && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /app  
WORKDIR /app  
  
ENTRYPOINT ["atlas-mvn"]  

