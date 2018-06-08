FROM rojima1/base  
  
USER root  
WORKDIR /home/root  
  
RUN apt-get update && \  
apt-get install -y \  
nodejs \  
npm && \  
npm install -g n && \  
n stable && \  
apt-get purge -y \  
nodejs \  
npm && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER developer  
WORKDIR /home/developer  

