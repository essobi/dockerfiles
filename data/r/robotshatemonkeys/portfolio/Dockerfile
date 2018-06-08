FROM ubuntu:latest  
  
# Install Utilities  
RUN apt-get update -q \  
&& apt-get install -yqq \  
apt-utils \  
cron \  
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
  
COPY . /usr/src/app/  
WORKDIR /usr/src/app/  
  
ONBUILD RUN npm install  
ONBUILD RUN npm run build  
  
ENV HOST 0.0.0.0  
ENV PORT 3000  
EXPOSE $PORT  
CMD [ "npm", "start" ]  

