FROM alpine:3.5  
RUN apk add --no-cache py2-pip  
  
RUN pip install b2  
  
COPY entry.sh /entry.sh  
  
WORKDIR /work  
  
ENTRYPOINT ["/entry.sh"]  

