FROM node  
  
MAINTAINER Jean-François Lépine <jeanfrancois@qualiboo.com>  
  
WORKDIR /var/tools  
  
# global packages  
RUN apt-get install -y make  
RUN npm install -g gemini gemini-gui  
  
# local installation  
RUN mkdir -p /var/tools  
RUN cd /var/tools && npm install gemini  
  
# Environment  
ENV NODE_PATH=/usr/local/lib/node_modules  
  
# Tools  
ADD Makefile /var/tools/  
  
WORKDIR /var/work  
ENTRYPOINT ["make", "-f", "/var/tools/Makefile"]

