FROM stackbrew/ubuntu:14.04  
MAINTAINER Evan Hazlett "<ejhazlett@gmail.com>"  
RUN echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main" >
/etc/apt/sources.list.d/node.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends node.js wget unzip  
RUN wget --no-check-certificate https://ghost.org/zip/ghost-0.4.2.zip -O
/tmp/ghost.zip && \  
unzip -d /ghost /tmp/ghost.zip && rm /tmp/ghost.zip  
RUN (cd /ghost && npm install --production)  
RUN (cd /ghost && sed "s/.*host:.*/\t\thost: '0.0.0.0',/g" config.example.js >
config.js)  
ENV NODE_ENV production  
WORKDIR /ghost  
VOLUME /ghost  
EXPOSE 2368  
CMD ["node", "/ghost/index.js"]  

