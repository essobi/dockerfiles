#  
# Dockerfile that builds an image containing an Nginx build that has been
patched to support "sticky-session" load balancing when used in conjunction
with Tomcat servers and derivatives.  
#  
# Author of this Dockerfile: Volkert de Buisonjé (volkertb)  
#  
# License of this Dockerfile: BSD 3-Clause
https://opensource.org/licenses/BSD-3-Clause  
#  
# Nginx license: BSD 2-Clause https://nginx.org/LICENSE  
# nginx-upstream-jvm-route license: BSD 3-Clause
https://opensource.org/licenses/BSD-3-Clause ( as referred to at
https://code.google.com/archive/p/nginx-upstream-jvm-route/ )  
#  
# To build:  
# docker build -t volkertb/nginx-upstream-jvm-route:1.6.3 .  
# To run (the --link values are examples):  
# docker run --name my-loadbalancer --link tomcat-container-node1:node1 --link
tomcat-container-node2:node2 -p 80:80 -p 443:443 -d volkertb/nginx-upstream-
jvm-route  
FROM centos:7  
RUN yum -y groupinstall 'Development Tools'  
RUN yum -y install wget  
WORKDIR /tmp  
RUN wget https://nginx.org/download/nginx-1.6.3.tar.gz  
RUN tar -zxvf nginx-1.6.3.tar.gz  
RUN mkdir nginx-upstream-jvm-route  
COPY ./config /tmp/nginx-upstream-jvm-route/  
COPY ./jvm_route.patch /tmp/nginx-upstream-jvm-route/  
COPY ./ngx_http_upstream_jvm_route_module.c /tmp/nginx-upstream-jvm-route/  
WORKDIR /tmp/nginx-1.6.3  
RUN patch -p0 < ../nginx-upstream-jvm-route/jvm_route.patch  
RUN yum -y install pcre-devel zlib-devel openssl-devel  
RUN ./configure --with-http_ssl_module --with-http_spdy_module --with-
http_realip_module --add-module=../nginx-upstream-jvm-route  
RUN make  
RUN make install  
  
# Check and verify if the built ngnix executable correctly parses the default
configuration file /usr/local/nginx/conf/nginx.conf  
RUN /usr/local/nginx/sbin/nginx -t  
  
# Copy the custom configuration file, overriding the default one:  
#COPY ./nginx.conf /usr/local/nginx/conf/  
# Copy the SSL/TLS certificate files:  
RUN mkdir /usr/local/nginx/ssl  
#COPY ./nginx.key /usr/local/nginx/ssl/  
#COPY ./nginx.crt /usr/local/nginx/ssl/  
# Check and verify the correctness of the configuration file
/usr/local/nginx/conf/nginx.conf  
# (Currently disabled, since it requires run-time container links to be
present during building.)  
#RUN /usr/local/nginx/sbin/nginx -t  
EXPOSE 80 443  
# Based on an explanation found at https://stackoverflow.com/a/26735742  
ENTRYPOINT ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]  

