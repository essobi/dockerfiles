FROM alpine:latest  
  
ENTRYPOINT ["aws"]  
  
RUN apk --no-cache add groff less python py-pip  
  
# install newest version of awscli available  
RUN pip install awscli  

