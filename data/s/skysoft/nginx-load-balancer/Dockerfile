FROM ubuntu:14.04  
  
WORKDIR /etc/nginx  
  
COPY nginx-common_1.8.0-1+trusty1_all.deb /root/nginx-
common_1.8.0-1+trusty1_all.deb  
COPY nginx-full_1.8.0-1+trusty1_amd64.deb /root/nginx-
full_1.8.0-1+trusty1_amd64.deb  
  
# installing tiller and dependencies and installing nginx and dependecies  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y update && apt-get -y upgrade && \  
apt-get -y install ruby && \  
gem install tiller && \  
apt-get -y install libgd3 && \  
apt-get -y install libgeoip1 && \  
apt-get -y install vim && \  
apt-get -y install libxml2 && \  
apt-get -y install libxslt1.1 && \  
apt-get -y install python && \  
dpkg -i /root/nginx-common_1.8.0-1+trusty1_all.deb && \  
dpkg -i /root/nginx-full_1.8.0-1+trusty1_amd64.deb && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# setting access log and error log to standard capture in docker  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# copy basic nginx conf  
#COPY conf.d /etc/nginx/conf.d  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY proxy_params.conf /etc/nginx/proxy_params.conf  
COPY certs /etc/nginx/certs  
  
# copy tiller conf  
COPY tiller /etc/tiller  
  
# setting default values for upstream configuration used with tiller to create
default server conf  
ENV upstream1 '172.22.186.126:9200'  
ENV upstream2 '172.22.186.125:9200'  
  
# settigng volumes and expose ports  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
EXPOSE 80 443  
  
# starts tiller which will configure and start nginx  
CMD ["/usr/local/bin/tiller" , "-v"]

