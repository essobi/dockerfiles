FROM java:latest  
  
ENV VERSION 3.1.1  
EXPOSE 5080 8081  
RUN set -ex; \  
cd /opt; \  
wget -q http://apache.crihan.fr/dist/openmeetings/$VERSION/bin/apache-
openmeetings-$VERSION.tar.gz; \  
tar zxf apache-openmeetings-$VERSION.tar.gz; \  
rm -f apache-openmeetings-$VERSION.tar.gz;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y swftools ffmpeg ghostscript imagemagick; \  
apt-get clean;  
  
WORKDIR /opt  
CMD ["./red5.sh"]  

