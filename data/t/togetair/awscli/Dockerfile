FROM library/alpine:latest  
  
RUN apk add --update \  
python \  
py-pip \  
groff  
  
RUN pip install awscli  
  
CMD ["aws"]  

