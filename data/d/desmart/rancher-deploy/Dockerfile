FROM alpine:3.7  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >>
/etc/apk/repositories \  
&& apk add --no-cache 'bash<4.4' \  
&& sed -i '$ d' /etc/apk/repositories  
  
RUN apk add --no-cache curl gettext jq docker  
  
COPY install/rancher-cli.sh /install/rancher-cli.sh  
RUN /install/rancher-cli.sh  
  
COPY install/rancher-compose.sh /install/rancher-compose.sh  
RUN /install/rancher-compose.sh  
  
COPY ./install/torus-cli.sh /install/torus-cli.sh  
RUN /install/torus-cli.sh \  
&& torus prefs set core.hints false \  
&& torus prefs set core.progress false  
  
COPY ./install/jo.sh /install/jo.sh  
RUN /install/jo.sh  
  
COPY ./bin /usr/bin  
  
SHELL ["/bin/bash"]  

