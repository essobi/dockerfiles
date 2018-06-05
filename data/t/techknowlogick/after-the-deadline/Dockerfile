FROM openjdk:9-jre  
  
ENV ATD_VERSION 081310  
RUN apt-get update -y && \  
apt-get install -y curl tar && \  
cd /srv && \  
curl
http://www.polishmywriting.com/download/atd_distribution${ATD_VERSION}.tgz |
tar -xz && \  
chmod -R a+x /srv/atd && \  
sed -i 's/127\\.0\\.0\\.1/0\\.0\\.0\\.0/g' /srv/atd/run.sh  
  
EXPOSE 1049  
WORKDIR /srv/atd  
  
CMD ./run.sh  

