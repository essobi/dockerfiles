FROM node:8.9.3-alpine  
  
MAINTAINER David Charbonnier <d.charbonnier@oxys.net>  
  
ENV project npm-proxy-cache  
  
RUN mkdir -p /opt/${project} /opt/${project}/bin && apk add --no-cache yarn  
WORKDIR /opt/${project}  
  
ADD package.json .  
  
RUN yarn install && \  
mkdir -p /opt/${project}/cache  
  
VOLUME /opt/${project}/cache  
  
ADD . .  
  
EXPOSE 8080  
ENTRYPOINT ["node", "/opt/npm-proxy-cache/bin/npm-proxy-cache"]  
  
CMD ["run"]

