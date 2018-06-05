FROM ubuntu:xenial  
ENV DUPLICATI_VERSION="2.0.2.1-1"  
ADD https://updates.duplicati.com/beta/duplicati_${DUPLICATI_VERSION}_all.deb
/  
RUN apt-get update &&\  
dpkg -i /duplicati_${DUPLICATI_VERSION}_all.deb||true &&\  
apt-get -f -y install &&\  
apt-get install tzdata &&\  
rm duplicati_${DUPLICATI_VERSION}_all.deb  
  
CMD ["duplicati-server","--webservice-interface=any","--webservice-
password=changeme"]  

