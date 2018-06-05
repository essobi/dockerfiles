FROM alpine:3.4  
MAINTAINER Dmitry Gavriloff <info@imega.ru>  
  
VOLUME ["/build", "/src", "/runner"]  
  
ADD build.sh /  
  
RUN apk --update add bash  
  
ENTRYPOINT ["/build.sh"]  

