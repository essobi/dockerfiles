## NginX Docker file  
## May 2016  
FROM nginx:latest  
MAINTAINER Thinh Huynh "thinhhc@gmail.com"  
# Add Ubuntu Trusty to sources.list  
RUN echo 'deb http://ftp.igh.cnrs.fr/pub/CRAN/bin/linux/ubuntu trusty/' >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9  
RUN apt-get update && apt-get -y upgrade  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Nginx  
RUN apt-get install -y nginx  
  
# Copy generated SSL Certs into ssl nginx/ssl dir  
RUN mkdir -p /etc/nginx/ssl  
ADD server.crt /etc/nginx/ssl  
ADD server.key /etc/nginx/ssl  
  
# Copy configuration file to nginx dir  
ADD site.conf /etc/nginx/conf.d/  
  
EXPOSE 443  

