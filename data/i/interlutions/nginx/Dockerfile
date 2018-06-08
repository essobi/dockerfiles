FROM nginx:1.14-alpine  
  
# Tools to change the uid on run  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk add --no-cache shadow su-exec  
COPY entrypoint-chuid /usr/local/bin  
  
ENTRYPOINT ["entrypoint-chuid"]  
CMD ["nginx", "-g", "daemon off;"]  

