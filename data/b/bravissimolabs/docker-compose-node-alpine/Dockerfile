ARG NODE_TAG=6.12.1-alpine  
FROM node:${NODE_TAG:-6.12.1-alpine}  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main >>
/etc/apk/repositories && \  
echo http://dl-cdn.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk add --update --no-cache docker py-pip git bash optipng gifsicle libjpeg-
turbo-utils && \  
pip install docker-compose && \  
rm -r ~/.cache/pip  
  
CMD /bin/bash  

