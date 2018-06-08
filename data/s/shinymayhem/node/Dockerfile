FROM node:4.1.2-slim  
  
RUN \  
npm install -g bower forever nodemon grunt-cli node-inspector && \  
mkdir -p /var/www && \  
useradd -ms /sbin/nologin node && \  
chown -R node:node /var/www  
  
#allow node user to run services on port 80 and 443 (when prefixed with
'authbind')  
RUN \  
apt-get update && \  
apt-get install -y authbind && \  
rm -rf /var/lib/apt/lists/* && \  
touch /etc/authbind/byport/443 && \  
touch /etc/authbind/byport/80 && \  
chown -R node:node /etc/authbind/byport/ && \  
chmod -R 755 /etc/authbind/byport/  
  
COPY deploy/run.sh /run.sh  
RUN chmod +x /run.sh  
  
WORKDIR /var/www/  
  
#set to effective working dir for default command (working_dir directive
doesn't work in tutum)  
ENV NODE_DIR /var/www/  
  
EXPOSE 80  
USER node  
  
CMD ["/run.sh"]  

