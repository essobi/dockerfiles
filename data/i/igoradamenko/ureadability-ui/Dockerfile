FROM node:4.5.0  
ENV APIPATH=/api  
  
ADD . /srv/ureadability-ui  
  
RUN \  
cd /srv/ureadability-ui && \  
npm i --only=production && \  
npm run build && \  
rm -rf ./node_modules ./dev /tmp/* && \  
mkdir -p /var/www && \  
mv ./public /var/www/webapp && \  
mv /srv/ureadability-ui/dockerinit.sh /init.sh && \  
chmod +x /init.sh  
  
VOLUME ["/var/www/webapp"]  
  
ENTRYPOINT ["/init.sh"]  
  
CMD ["sleep", "100"]  

