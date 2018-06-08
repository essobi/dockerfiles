FROM alpine:edge  
  
MAINTAINER rogueosb@gmail.com  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --update mono@testing curl wget bash zip sqlite bzip2 \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /app \  
&& mkdir /config \  
&& mozroots --import --ask-remove  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
VOLUME /config  
EXPOSE 3579  
WORKDIR /config  
  
ENTRYPOINT ["/start.sh"]  

