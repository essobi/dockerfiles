FROM ubuntu:latest  
  
# Install Utilities  
RUN apt-get update -q \  
&& apt-get install -yqq \  
apt-utils \  
curl \  
vim \  
sudo \  
make \  
gcc \  
libkrb5-dev \  
build-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -yq nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create Required Folders  
RUN mkdir -p /usr/api  
RUN mkdir -p /usr/api/temp  
  
COPY . /usr/api  
WORKDIR /usr/api  
  
RUN npm install --production  
  
ENV PORT 8082  
EXPOSE $PORT  
  
  
CMD ["npm", "start"]  

