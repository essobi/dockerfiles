FROM node:0.12  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
RUN git clone https://github.com/c9/core.git /cloud9 && \  
cd /cloud9 && ./scripts/install-sdk.sh  
  
RUN npm install hexo-cli -g  
  
RUN wget -O - https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz
| tar -xzC /usr/local -f - && \  
echo "export GOPATH=/workspace/gocode" >> /root/.profile && \  
echo "export PATH=$PATH:/usr/local/go/bin:/workspace/gocode/bin" >>
/root/.profile  
  
WORKDIR /workspace  
  

