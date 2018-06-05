FROM phusion/baseimage:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY etc/apt/sources.list /etc/apt/sources.list  
RUN apt-get update; apt-get install -yy htop nginx php5-fpm php5-cli php5-gd
php5-mysql --no-install-recommends; apt-get clean; rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
COPY ttrss /ttrss  
COPY etc /etc  
  
EXPOSE 80  
CMD ["/sbin/my_init"]  

