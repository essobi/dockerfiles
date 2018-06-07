FROM node:4.6.0  
RUN useradd -m -s /bin/bash casperjs  
USER casperjs  
  
ENV PHATOMJS_VERSION=2.1.1 \  
PHATOMJS_HOME=/home/casperjs/phantomjs-2.1.1-linux-x86_64 \  
CASPERJS_HOME=/home/casperjs/node_modules/casperjs \  
CASPERJS_VERSION=1.1.3  
ENV PATH=$PHATOMJS_HOME/bin:$CASPERJS_HOME/bin:$PATH  
  
# install phatomjs  
RUN cd /home/casperjs \  
&& curl -L -O
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar -xf phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& rm ./phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& npm install casperjs@1.1.3  
  
WORKDIR /home/casperjs/work  
  
ENTRYPOINT ["casperjs"]  
CMD ["selftest"]  

