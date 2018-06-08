FROM debian:stretch  
  
RUN set -ex ;\  
apt-get update ;\  
apt-get install -y apt-transport-https ;\  
echo "deb https://packages.inverse.ca/SOGo/nightly/4/debian/ stretch stretch"
>> /etc/apt/sources.list ;\  
apt-get update ;\  
apt-get install -y --allow-unauthenticated sogo  
  
EXPOSE 20000  
  
CMD [ "sogod", "-WONoDetach", "YES", "-WOPort", "20000", "-WOLogFile", "-",
"-WOPidFile", "/run/sogo.pid"]  

