FROM node:0.10  
  
ENV PHANTOMJS_VERSION 1.9.8  
  
ENV PHANTOMJS_ID phantomjs-${PHANTOMJS_VERSION}-linux-x86_64  
ENV PHANTOMJS_TAR ${PHANTOMJS_ID}.tar.bz2  
  
RUN apt-get update ;\  
apt-get -y install libfreetype6 libfreetype6-dev fontconfig ;\  
\  
curl -L https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOMJS_TAR} -o
/tmp/${PHANTOMJS_TAR} ;\  
tar -xjf /tmp/${PHANTOMJS_TAR} -C /tmp/ ;\  
mv /tmp/${PHANTOMJS_ID}/bin/phantomjs /usr/local/bin/phantomjs ;\  
\  
rm -rf /var/lib/cache /var/lib/log /tmp/*  

