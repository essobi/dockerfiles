FROM thenextapps/nginxphp:v1  
MAINTAINER thenextapps@gmail.com  
  
ADD nginxserver /etc/nginx/sites-available/nginxserver  
  
# Add link to an entry in sites-enabled from sites-available  
WORKDIR /etc/nginx/sites-enabled  
  
# RUN command has effect on WORKDIR  
RUN ln -s ../sites-available/nginxserver  
  
# Add hostfile  
ADD hostsfile.sh /tmp/hostsfile.sh  
RUN chmod +x /tmp/hostsfile.sh  
  
# Add start server file  
ADD start-server.sh /tmp/start-server.sh  
RUN chmod +x /tmp/start-server.sh  
  
WORKDIR /srv/www/public  
  
CMD /tmp/start-server.sh && /sbin/my_init && sudo service postfix start  
  
EXPOSE 8089 8090 8091  

