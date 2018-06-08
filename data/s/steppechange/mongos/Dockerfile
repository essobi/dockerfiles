FROM mongo:3.4.2  
RUN apt-get update && apt-get -y upgrade && apt-get -y install \  
wget \  
curl  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/bin; wget
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O jq;
chmod +x jq  
  
ADD onstart.sh /root/onstart.sh  
  
ENTRYPOINT ["/root/onstart.sh"]  

