FROM java:8-jre  
MAINTAINER Dries De Peuter <dries@depeuter.io>  
  
RUN UNATTENDED=true bash -c "$(curl -sSL
https://download.newrelic.com/npi/release/install-npi-linux-debian-x64.sh)"  
  
WORKDIR /root/newrelic-npi  
RUN ./npi fetch com.tylerhoersch.nr.cassandra -y  
  
COPY plugin.json ./plugin.json  
COPY start.sh ./start.sh  
  
ENTRYPOINT ["./start.sh"]  
CMD ["newrelic-cassandra"]  

