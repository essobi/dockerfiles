FROM alpine:edge  
  
ENV TRANSMISSION_CLI_VERSION="2.94 (d8e60ee44f)"  
RUN apk add \--no-cache transmission-cli  
  
ENV HOME /home/user  
  
RUN adduser -u 1000 -D user \  
&& chown -R user:user $HOME  
  
WORKDIR $HOME  
  
USER user  
  
ENTRYPOINT ["/usr/bin/transmission-remote"]  

