FROM python:3.6  
MAINTAINER Alexander Polesov <dev@alex-web.ru>  
  
RUN pip install redis flower  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["flower", "--port=5555"]  

