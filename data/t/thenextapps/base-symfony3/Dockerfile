FROM thenextapps/nginxphp:v1  
MAINTAINER thenextapps@gmail.com  
  
# Add symfony installer  
RUN curl -LsS http://symfony.com/installer -o /usr/local/bin/symfony  
RUN chmod a+x /usr/local/bin/symfony  
  
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
  
# Add tmp folder for vendor  
RUN mkdir -p /tmp/symfony3/vendor  
RUN chmod -R 777 /tmp/symfony3/*  
  
WORKDIR /srv/www/symfony3  
  
CMD /tmp/start-server.sh && /sbin/my_init && sudo service postfix start  
  
EXPOSE 8089 8090 8091  

