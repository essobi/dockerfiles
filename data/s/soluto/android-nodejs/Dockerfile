FROM soluto/android:26-4.6  
RUN adduser --disabled-password --gecos '' soluto  
RUN usermod -aG sudo soluto  
  
ENV NODEJS_VERSION=8.9.3 \  
PATH=$PATH:/opt/node/bin \  
YARN_VERSION=1.3.2  
WORKDIR "/opt/node"  
  
RUN apt-get update && apt-get install -y curl ca-certificates --no-install-
recommends && \  
apt-get install -y git && \  
apt-get install -y bzr && \  
apt-get install -y g++ && \  
apt-get install -y build-essential && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
RUN curl -sL
https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz
| tar xz --strip-components=1  
RUN npm install -g yarn@${YARN_VERSION}  
  
WORKDIR "/"  
CMD bash  

