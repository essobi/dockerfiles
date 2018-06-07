FROM gliderlabs/alpine  
  
RUN apk update  
RUN apk add mini_httpd  
COPY content /usr/share/mini_httpd  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mini_httpd", "-d", "/content", "-D"]  
  
VOLUME /content  

