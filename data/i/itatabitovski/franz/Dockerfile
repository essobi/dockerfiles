FROM itatabitovski/debian:jessie  
  
ENV FRANZ_VERSION 4.0.4  
RUN apt-install wget \  
libgtk2.0-0 \  
libxtst6 \  
libxss1 \  
libgconf-2-4 \  
libnss3 \  
libasound2 \  
alsa-utils && \  
mkdir /opt/franz && cd /opt/franz && \  
wget https://github.com/meetfranz/franz-
app/releases/download/$FRANZ_VERSION/Franz-linux-x64-$FRANZ_VERSION.tgz && \  
tar xf Franz*.tgz && rm Franz*.tgz  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

