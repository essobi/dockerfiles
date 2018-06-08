FROM vanb777/ffmpeg-sox  
  
RUN apt-get update -y && \  
apt-get install -y build-essential curl  
  
RUN curl -sL https://deb.nodesource.com/setup_0.10 | bash - && \  
apt-get install -y nodejs && \  
node --version && npm --version  

