FROM node:7.5.0-alpine  
  
USER 0  
WORKDIR /opt  
  
RUN apk update \  
&& apk add git vim curl wget bash \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g spectacle-docs  
  
COPY entrypoint.sh entrypoint.sh  
COPY is_logo.svg is_logo.svg  
ENTRYPOINT ["/opt/entrypoint.sh"]  

