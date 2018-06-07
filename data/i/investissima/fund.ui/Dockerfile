FROM otassel/nodejs  
  
MAINTAINER Olivier TASSEL <olivier.tassel@investissima.com>  
  
COPY nodejs /var/src  
  
# Deployment  
RUN npm install  
  
# NewRelic Server Monitoring  
COPY entrypoint.sh /usr/bin/  
RUN chmod +x /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
CMD ["npm", "start"]

