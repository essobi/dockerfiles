FROM python:2-alpine  
RUN apk add --update --no-cache openssl  
COPY phishthis.py docker-entrypoint.sh /usr/local/bin/  
ENV PYTHONUNBUFFERED=x  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["phishthis.py"]  

