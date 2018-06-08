FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash - && \  
apt-get install -y nodejs && \  
npm install -y -g nodemon && \  
npm install -y -g express && \  
npm install -y -g express-generator && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y libzmq-dev && \  
apt-get install -y libevent-dev  
  
RUN apt-get install -y python  
  
RUN apt-get install -y build-essential  
  

