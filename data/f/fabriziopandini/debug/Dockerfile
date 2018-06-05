FROM fabriziopandini/pause:alpine  
MAINTAINER Fabrizio Pandini <fabrizio.pandini@gmail.com>  
  
RUN apk add --update --no-cache curl python3 iputils net-tools  
RUN pip3 install --upgrade pip setuptools httpie  
  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/local/bin/jq  
RUN chmod 0755 /usr/local/bin/jq

