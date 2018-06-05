FROM orangesys/alpine-kong:0.9.4  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
RUN mkdir -p /etc/kong/  
COPY kong.conf /etc/kong/  
COPY nginx.conf /etc/kong/  
  
EXPOSE 8000 8443 8001 7946  
CMD ["kong", "start", "--conf", "/etc/kong/kong.conf", "--nginx-conf",
"/etc/kong/nginx.conf"]

