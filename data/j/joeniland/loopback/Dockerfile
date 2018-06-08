FROM alpine:edge  
  
MAINTAINER Joe Niland <joe@originalmind.com.au>  
  
RUN set -x \  
&& apk --update add \  
build-base \  
python2 \  
nodejs \  
git  
  
RUN npm install -g --silent apiconnect  
RUN npm install -g --silent --python=python2.7 strongloop  
RUN npm install -g --silent gulp yo  
# Add additional generators here  
# Add non-root user for dev work  
RUN adduser -u 501 dev -D -s /bin/ash  
# && \  
# chmod -R dev:dev /app  
USER dev  
  
# ports: node apiconnect  
EXPOSE 3000 4001  
VOLUME ["/app"]  
WORKDIR /app  

