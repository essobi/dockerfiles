FROM java:8-jre  
MAINTAINER Rafael Bernardo <rafael@meupatrocinio.com>  
  
RUN UNATTENDED=true bash -c "$(curl -sSL
https://download.newrelic.com/npi/release/install-npi-linux-debian-x64.sh)"  
  
WORKDIR /root/newrelic-npi  
RUN ./npi fetch me.snov.newrelic-elasticsearch -y  
  
COPY plugin.json ./plugin.json  
COPY start.sh ./start.sh  
  
ENTRYPOINT ["./start.sh"]  
CMD ["newrelic-elasticsearch"]  

