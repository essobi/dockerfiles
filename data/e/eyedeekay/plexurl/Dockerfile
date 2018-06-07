FROM alpine:edge  
RUN apk update  
RUN apk add python3 darkhttpd  
#RUN apk add python py2-pip darkhttpd  
RUN adduser -D -h /home/plexurl plexurl  
RUN chown -R plexurl:plexurl /home/plexurl && umask 002 /home/plexurl  
COPY . /home/plexurl/plexurl/  
WORKDIR /home/plexurl/plexurl  
RUN pip3 install --exists-action w -e .  
USER plexurl  
ENTRYPOINT [ "sh", "-i", "-c" ]  
  

