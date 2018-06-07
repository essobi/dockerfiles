FROM phusion/baseimage  
MAINTAINER "Jaigouk Kim" <ping@jaigouk.kim>  
  
RUN echo "update system and install confd" \  
&& apt-get update -y -qq \  
&& apt-get install -y -qq nginx curl \  
&& rm /etc/nginx/sites-enabled/default \  
&& rm /etc/nginx/nginx.conf \  
&& cd /usr/local/bin \  
&& echo "install confd" \  
&& curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-
amd64 -o confd \  
&& chmod +x confd \  
&& mkdir -p /etc/confd/{conf.d,templates}  
  
ADD ./conf/nginx.toml /etc/confd/conf.d/  
ADD ./conf/nginx.tmpl /etc/confd/templates/  
ADD ./conf/nginx.conf /etc/nginx/  
ADD ./conf/confd-watch /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/confd-watch

