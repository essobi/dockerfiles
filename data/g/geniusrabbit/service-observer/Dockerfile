FROM alpine:latest  
MAINTAINER GeniusRabbitCo (Dmitry Ponomarev <demdxx@gmail.com>)  
  
COPY /observer /  
  
ENV REGISTRY_DNS=http://registry:8500/dc1?refresh_interval=5  
ENV CHECK_HTTP=http://{{address}}/healthcheck  
CMD ["/observer", "--listen", ":8080"]  
EXPOSE 8080

