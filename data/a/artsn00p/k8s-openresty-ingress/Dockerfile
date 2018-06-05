ARG ARCH=amd64  
# Build go binary  
FROM golang AS gobuild  
  
COPY ./ /go/src/github.com/meyskens/k8s-openresty-ingress  
WORKDIR /go/src/github.com/meyskens/k8s-openresty-ingress/controller  
  
ARG GOARCH=amd64  
ARG GOARM=6  
RUN GOARCH=${GOARCH} GOARM=${GOARM} go build ./  
  
# Set up deinitive image  
FROM openresty/openresty:xenial  
  
RUN apt-get update -y || apt-get install -y openssl openssl-dev  
  
# Add Dummy cert for dummy conf  
RUN openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 \  
-subj '/CN=sni-support-required-for-valid-ssl' \  
-keyout /etc/ssl/resty-auto-ssl-fallback.key \  
-out /etc/ssl/resty-auto-ssl-fallback.crt  
  
COPY \--from=gobuild /go/src/github.com/meyskens/k8s-openresty-
ingress/controller/controller /usr/local/bin/controller  
  
COPY ./config/default/ /etc/nginx/  
  
COPY ./template/ingress.tpl /etc/nginx/ingress.tpl  
ENV OPENRESTY_TEMPLATEPATH=/etc/nginx/ingress.tpl  
ENV OPENRESTY_INGRESSATH=/etc/nginx/sites/  
  
EXPOSE 80  
EXPOSE 443  
CMD controller  

