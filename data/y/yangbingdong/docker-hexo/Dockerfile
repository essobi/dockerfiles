FROM ubuntu:16.04  
MAINTAINER yangbingdong <yangbingdong1994@gmail.com>  
  
USER root  
  
ENV NODE_VERSION 8.9.4  
ENV NODE_DIR /opt/nodejs  
ENV HOXO_DIR /root/hexo  
  
RUN apt-get update && \  
apt-get install -y git curl && \  
mkdir ${NODE_DIR} && \  
curl -L
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
| tar xvzf - -C ${NODE_DIR} \--strip-components=1  
  
ENV PATH $PATH:${NODE_DIR}/bin  
  
RUN npm install -g hexo-cli  
  
ENV PATH $PATH:${NODE_DIR}/bin  
  
RUN cd /root && \  
hexo init hexo && \  
cd hexo && \  
git clone https://github.com/iissnan/hexo-theme-next themes/next && \  
npm install && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/root/hexo/source/_posts"]  
  
WORKDIR /root/hexo  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

