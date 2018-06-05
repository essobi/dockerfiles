FROM mongo:3.4  
MAINTAINER Analyser, analyser@gmail.com  
  
USER root  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN ln -f -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards
compat  
  
USER mongodb  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 27017  
CMD ["mongod"]  

