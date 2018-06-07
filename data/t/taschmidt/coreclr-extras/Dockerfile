FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs && \  
npm set progress=false && \  
npm install -g gulp@3.9.1 && \  
npm install -g bower@1.7.7  

