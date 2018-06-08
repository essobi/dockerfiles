FROM node:6  
RUN apt-get update && \  
apt-get -y install software-properties-common git-core build-essential
automake unzip python-dev python-setuptools supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone -b v4.5.0 https://github.com/facebook/watchman.git /tmp/watchman  
WORKDIR /tmp/watchman  
RUN ./autogen.sh  
RUN ./configure  
RUN make  
RUN make install  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install || true  
  
RUN mkdir -p /usr/local/var/run/watchman/  
  
EXPOSE 8081  

