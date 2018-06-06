FROM phusion/baseimage:0.10.0  
LABEL maintainer="Graham Stewart <graham.stewart@findyourcanopy.com>"  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn && \  
  
apt-get install -y graphicsmagick && \  
  
npm install -g nodemon@1.10.2 && \  
npm install -g apidoc@0.16.1 && \  
  
mkdir -p /opt/app && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH /opt/app/node_modules/.bin:$PATH  
CMD ["/sbin/my_init"]  
  

