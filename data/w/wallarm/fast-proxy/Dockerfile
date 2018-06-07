FROM golang:1.6 as builder  
  
RUN curl https://glide.sh/get | sh  
  
COPY glide.yaml /go/src/github.com/wallarm/docker-wallarm-fast-
proxy/glide.yaml  
COPY glide.lock /go/src/github.com/wallarm/docker-wallarm-fast-
proxy/glide.lock  
COPY proxy.go /go/src/github.com/wallarm/docker-wallarm-fast-proxy  
  
RUN cd /go/src/github.com/wallarm/docker-wallarm-fast-proxy \  
&& glide install && go build -o /usr/local/bin/proxy  
  
FROM wallarm/node  
  
RUN mkdir -p /etc/wallarm/proxy  
COPY bin/ /usr/local/bin/  
COPY wallarm/ /etc/wallarm/  
COPY nginx/vhost /etc/nginx-wallarm/sites-enabled/default  
COPY nginx/proxy_params /etc/nginx-wallarm/  
COPY nginx/logs.conf /etc/nginx-wallarm/conf.d/  
COPY supervisord.conf /etc/supervisor/  
COPY ./script/set_marker /usr/local/bin/set_marker  
COPY ./script/set_policy /usr/local/bin/set_policy  
  
COPY \--from=0 /usr/local/bin/proxy /usr/local/bin/proxy  

