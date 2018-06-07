FROM phusion/passenger-ruby22  
  
ENV HOME /root  
  
CMD ["/sbin/my_init"]  
#################################  
RUN rm -f /etc/service/nginx/down \  
&& rm /etc/nginx/sites-enabled/default \  
&& mkdir /home/app/webapp \  
&& echo "gzip_comp_level 9;" > /etc/nginx/conf.d/gzip_max.conf \  
&& apt-get update && apt-get install -y redis-server  
  
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf  
ADD . /home/app/webapp  
  
EXPOSE 80  
#################################  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

