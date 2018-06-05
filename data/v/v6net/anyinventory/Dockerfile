FROM alpine:latest  
  
MAINTAINER Cougar <cougar@random.ee>  
  
RUN apk add --no-cache php5-cli php5-mysql php5-gd php5-pear git  
RUN pear install DB  
  
RUN git clone https://github.com/version6net/anyInventory  
  
COPY run.sh /run.sh  
RUN chmod u+rwx /run.sh  
  
VOLUME /sessions  
  
EXPOSE 80  
ENV PHP_UPLOAD_MAX_FILESIZE=64M PHP_MAX_INPUT_VARS=2000  
ENTRYPOINT [ "/run.sh" ]  

