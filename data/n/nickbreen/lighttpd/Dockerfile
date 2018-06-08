FROM phusion/baseimage:0.9.18  
  
MAINTAINER Nick Breen <nick@foobar.net.nz>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
lighttpd && apt-get clean  
  
COPY *.conf /etc/lighttpd/conf-available/  
  
RUN lighttpd-enable-mod fastcgi php expire syslog  
  
COPY run /etc/service/lighttpd/  
  
RUN FASTCGI_PORT_9000_TCP_ADDR="127.0.0.1" FASTCGI_PORT_9000_TCP_PORT="9000"
/etc/service/lighttpd/run -t  
  
EXPOSE 80  

