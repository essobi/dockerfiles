FROM node:8-alpine  
  
ENV ADDICT_VERSION jceloria/addict  
  
RUN apk add --no-cache git strace \  
&& npm install "addict@$ADDICT_VERSION" \--production -g \  
&& npm cache clear --force \  
&& apk del git  
  
WORKDIR /usr/local/lib/node_modules/addict  
  
EXPOSE 3000  
ENTRYPOINT [ "/usr/local/bin/addict" ]  

