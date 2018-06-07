FROM dockerfile/nodejs  
MAINTAINER Yosh de Vos "yosh@elzorro.nl"  
# Install Ghost  
RUN \  
cd /tmp && \  
wget https://ghost.org/zip/ghost-latest.zip && \  
unzip ghost-latest.zip -d /ghost && \  
rm -f ghost-latest.zip && \  
cd /ghost && \  
npm install --production && \  
useradd ghost --home /ghost  
  
# Add config file  
ADD config.js /ghost/config.js  
  
# Set environment variables.  
ENV NODE_ENV production  
ENV URL http://localhost:2368/  
ENV DB_CLIENT mysql  
ENV DB_HOST db  
ENV DB_PORT 3306  
ENV DB_USER ghost  
ENV DB_PASSWORD ghost  
ENV DB_DATABASE ghost  
  
# Define working directory.  
WORKDIR /ghost  
  
# Set volume  
VOLUME "/ghost/content"  
  
# Add run script  
ADD run-ghost.sh /run-ghost.sh  
RUN chmod 0500 /run-ghost.sh  
  
EXPOSE 2368  
CMD ["/run-ghost.sh"]  

