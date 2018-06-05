FROM python:2.7  
COPY docker-entrypoint.sh /usr/local/bin  
  
RUN wget https://raw.github.com/henzk/ape/master/bin/bootstrape -O
/usr/local/bin/bootstrape && \  
chmod 0755 /usr/local/bin/bootstrape  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["ape"]  
  
VOLUME ["/code"]  

