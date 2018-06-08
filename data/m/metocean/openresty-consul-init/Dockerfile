FROM openresty/openresty:1.11.2.4-alpine  
MAINTAINER "Greg Chalmers" <g.chalmers@metocean.co.nz>  
  
RUN apk update &&\  
apk upgrade &&\  
apk add --no-cache curl iputils ca-certificates make gcc musl-dev  
  
ENV CONSUL_VERSION=0.7.5  
RUN cd /tmp &&\  
curl -o consul.zip -L
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
&&\  
unzip consul.zip &&\  
chmod +x consul &&\  
mv consul /usr/bin &&\  
mkdir /consul &&\  
rm -rf /tmp/*  
  
ADD ./nginx/include/* /usr/local/openresty/nginx/conf/  
ADD ./lua/cors /usr/local/openresty/nginx/lua/cors  
  
ADD ./init /src/init  
RUN cd /src/init && make && cp init /bin/  
  
ENTRYPOINT ["/bin/init"]  

