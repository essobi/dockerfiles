FROM google/cloud-sdk  
  
MAINTAINER Akshaya Acharya <akshaya@hasura.io>  
  
COPY logforward.sh /  
  
RUN chmod +x /logforward.sh  
  
ENTRYPOINT ["/logforward.sh"]  

