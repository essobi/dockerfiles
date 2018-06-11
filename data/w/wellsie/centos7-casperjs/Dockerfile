FROM wellsie/centos7-phantomjs  
MAINTAINER Jono Wells <_oj.io>  
  
ENV CASPERJS_VERSION 1.1.0-beta3  
  
RUN cd /usr/local && \  
git clone -b phantomjs-2 https://github.com/n1k0/casperjs.git && \  
ln -s /usr/local/casperjs/bin/casperjs /usr/bin/casperjs  
  
VOLUME /mnt/test  
WORKDIR /mnt/test  
  
CMD [ "/usr/bin/casperjs" ]  

