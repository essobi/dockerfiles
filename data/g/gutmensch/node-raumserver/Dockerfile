FROM mhart/alpine-node:8  
WORKDIR /  
  
RUN set -x \  
&& apk update \  
&& apk add --no-cache nginx  
  
# If you have native dependencies, you'll need extra tools  
# RUN apk add --no-cache make gcc g++ python  
RUN set -x \  
&& npm install node-raumserver  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz
/tmp/  
RUN set -x \  
&& gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /  
  
COPY ./manifest/ .  
  
# XXX: patch for broken template path. lots of trailing whitespace and windows
line feeds, yummy.  
RUN set -x \  
&& cd /node_modules \  
&& patch -p1 < /config/setUriMetadata_fix_path.patch  
  
EXPOSE 3000 3535  
ENTRYPOINT ["/init"]  
  

