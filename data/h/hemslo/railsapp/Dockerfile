FROM phusion/passenger-customizable:0.9.15  
MAINTAINER Hemslo <hemslo.wang@gmail.com>  
  
RUN /pd_build/ruby2.2.sh  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
cmake \  
&& apt-get install -y -o Dpkg::Options::="--force-confold" passenger nginx-
extras \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN npm install -g bower  
RUN rm /etc/nginx/sites-enabled/default  
COPY nginx_conf_d.conf /etc/nginx/conf.d/default.conf  
RUN rm -f /etc/service/sshd/down  
RUN rm -f /etc/service/nginx/down  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/ssl", "/var/log/nginx",
"/home/app/.ssh"]  
  
CMD ["/sbin/my_init"]  
EXPOSE 22 80 443  

