FROM python:3-alpine  
  
RUN apk update  
RUN apk add nodejs  
RUN npm install -g elasticdump  
RUN pip install awscli  
  
COPY run_elasticdump.sh /run_elasticdump.sh  
CMD ["/run_elasticdump.sh"]  

