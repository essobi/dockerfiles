FROM alpine:latest  
  
RUN apk add \--update pidgin pidgin-lang pidgin-sipe pidgin-sipe-lang
ghostscript-fonts && \  
adduser -h /home/pidgin -u 1000 -D pidgin  
  
USER pidgin  
  
ENTRYPOINT [ "pidgin" ]  
  
CMD [ "-c", "/home/pidgin/config" ]

