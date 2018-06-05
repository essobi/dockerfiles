FROM golang:alpine as builder  
  
# install dependencies  
RUN apk add -U git  
  
# install hugo  
RUN cd /srv \  
&& wget
https://github.com/gohugoio/hugo/releases/download/v0.38/hugo_0.38_Linux-64bit.tar.gz
\  
&& tar xf ./hugo_0.38_Linux-64bit.tar.gz \  
&& mv ./hugo /usr/local/bin/hugo \  
&& rm -rf /srv/*  
  
WORKDIR /go/src/github.com/codeepblue/blog  
  
COPY . .  
  
RUN hugo  
  
FROM nginx:alpine  
  
COPY \--from=builder /go/src/github.com/codeepblue/blog/public
/usr/share/nginx/html  
  
EXPOSE 80 443  

