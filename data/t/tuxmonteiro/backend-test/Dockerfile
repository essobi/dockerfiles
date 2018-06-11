FROM ubuntu:vivid  
  
MAINTAINER Marcelo Teixeira Monteiro  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
ENV INITRD no  
  
WORKDIR /root  
  
RUN apt-get install -y nginx ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /srv/html && \  
if [ ! -f /srv/html/index.html ]; then \  
dd if=/dev/urandom bs=1 count=64 | base64 -w0 | cut -c1-63 2> /dev/null >
/srv/html/index.html; \  
fi && \  
if [ ! -f /srv/html/5.html ]; then \  
dd if=/dev/urandom bs=1M count=5 | base64 -w0 | cut -c1-5242879 2> /dev/null >
/srv/html/5.html; \  
fi  
  
ADD nginx.conf /etc/nginx/  
  
EXPOSE 8081 8082 8083 8084  
CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]  

