FROM almir/webhook  
  
RUN apk add --update curl python2 make py-pip  
RUN pip install docker-compose  
RUN rm -rf ~/.cache/pip  
  
EXPOSE 9000  
ENTRYPOINT ["/usr/local/bin/webhook"]  

