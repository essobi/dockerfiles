FROM alpine  
MAINTAINER Frederic Branczyk <fbranczyk@gmail.com>  
  
RUN apk --update add git && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /git  
COPY script.sh /git/script.sh  
  
ENTRYPOINT ["/git/script.sh"]  
  

