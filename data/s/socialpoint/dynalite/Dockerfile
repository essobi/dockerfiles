FROM node:8.2-alpine  
  
LABEL maintainer "Backend Team <backend@socialpoint.es>"  
  
ENV DYNALITE_VERSION=1.2.0  
RUN apk add --no-cache --virtual .gyp \  
python \  
make \  
g++ \  
&& npm --unsafe-perm install --no-optional \  
-g dynalite@${DYNALITE_VERSION} \  
-g leveldown@1.5.3 \  
&& npm --force cache clear \  
&& rm -rf /tmp/* /var/tmp/* \  
&& apk del .gyp  
  
RUN mkdir -p /var/dynamodb  
  
EXPOSE 8000  
VOLUME /var/dynamodb  
  
CMD ["dynalite", "--port=8000", "--createTableMs=100", "--deleteTableMs=100",
"--updateTableMs=100", "--path=/var/dynamodb"]  

