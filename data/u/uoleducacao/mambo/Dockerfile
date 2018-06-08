FROM uoleducacao/node:8  
  
RUN apt-get update && \  
apt-get install -y unoconv && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ && \  
HOME=/tmp unoconv --listener  

