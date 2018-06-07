FROM node:8  
RUN apt-get update && apt-get install -y apt-transport-https  
  
RUN mkdir -p /var/log/node/  
RUN mkdir -p /opt/server  
  
# Install Yarn and Git  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
RUN apt-get install -y git yarn  
  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
VOLUME /opt/server/  
  
CMD ["/start.sh"]

