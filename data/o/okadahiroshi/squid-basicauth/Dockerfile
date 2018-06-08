FROM alpine:3.4  
  
# update and install squid  
RUN apk update &&\  
apk add squid &&\  
apk upgrade  
# copy mini_htpasswd from mini_http package  
RUN mkdir -p /tmp/mini_httpd &&\  
cd /tmp/mini_httpd &&\  
apk fetch mini_httpd &&\  
tar xvzf mini_httpd-* &&\  
mv ./usr/sbin/mini_htpasswd /usr/sbin &&\  
cd / &&\  
rm -rf /tmp/mini_httpd  
  
# Rewrite settings in squid.conf file  
ADD squid.conf.patch /tmp  
RUN cd /etc/squid &&\  
patch squid.conf /tmp/squid.conf.patch &&\  
rm /tmp/squid.conf.patch  
  
# Add entrypoint.sh  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
## copy utility fiels (development only)  
#RUN apk add vim  
#  
## make workdir  
#RUN mkdir -p /root/work  

