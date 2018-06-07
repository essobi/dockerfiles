FROM alpine:3.3  
  
RUN apk add --update \  
git \  
nodejs \  
python \  
make \  
g++ && \  
npm install -g node-gyp && \  
npm config set cache "/cache/npm" \--global && \  
npm config set cache-min 100000000 \--global && \  
rm -rf /var/cache/apk/*  
  
COPY ./entry.sh /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  

