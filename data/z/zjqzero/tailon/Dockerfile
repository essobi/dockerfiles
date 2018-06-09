FROM alpine:latest  
  
MAINTAINER zhoujunqian <zjqzero@gmail.com>  
  
COPY config.yml /etc/tailon/config.yml  
RUN apk update  
RUN apk add python py-pip grep gawk  
RUN pip install tailon  
RUN rm -rf /bin/grep  
RUN rm -rf /var/cache/apk/*  
  
EXPOSE 80  
CMD ["tailon", "-c", "/etc/tailon/config.yml"]  

