FROM adaptris/interlok:snapshot-alpine  
  
RUN rm -rf /opt/interlok/webapps/*.war  
  
ADD config /opt/interlok/config  
ADD docker-entrypoint-wrapper.sh /docker-entrypoint-wrapper.sh  
  
ENTRYPOINT ["/docker-entrypoint-wrapper.sh"]  
CMD [""]  

