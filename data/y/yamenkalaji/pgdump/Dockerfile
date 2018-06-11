FROM alpine  
  
RUN apk add --update postgresql-client bash  
  
COPY dump.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/dump.sh  
  
RUN mkdir /code/  
  
WORKDIR /code/  
  
CMD dump.sh

