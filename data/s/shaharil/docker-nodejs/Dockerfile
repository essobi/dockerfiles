FROM debian:jessie  
RUN \  
apt-get update &&\  
apt-get install -y curl sudo make wget nano git bzip2 nginx supervisor  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - ; apt-get
install -y nodejs  
RUN npm install -g gulp  
RUN rm -rf /var/lib/apt/lists/*  

