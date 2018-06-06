FROM debian:jessie  
MAINTAINER Franz Bund "ich.bin@derfranz.eu"  
ENV MICROEMU="microemulator-2.0.4"  
ENV DOWNLOAD_URL_MICROEMU="https://storage.googleapis.com/google-code-archive-
downloads/v2/code.google.com/microemu/${MICROEMU}.zip"  
ENV DOWNLOAD_URL_OPERAMINI="http://mini.opera.com/download-7/opera-mini-
latest-advanced-en.jar?no_redir&ismobile=false"  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
RUN \  
apt-get update && \  
apt-get install -y wget unzip default-jre  
  
RUN \  
cd /home/user/ && \  
wget ${DOWNLOAD_URL_MICROEMU} && \  
unzip ${MICROEMU}.zip && \  
mkdir microemulator && mv ${MICROEMU}/* microemulator && rm -rf ${MICROEMU} &&
cd microemulator && \  
mkdir midlets && cd midlets && \  
wget --content-disposition ${DOWNLOAD_URL_OPERAMINI}  
  
RUN \  
apt-get purge -y --auto-remove wget unzip && \  
rm -rf /var/lib/apt/lists/*  
  
USER user  
WORKDIR /home/user/microemulator  
VOLUME /home/user/microemulator/midlets  
  
CMD java -jar microemulator.jar --resizableDevice 320 480 midlets/*.jar  

