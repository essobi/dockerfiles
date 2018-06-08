FROM ubuntu:trusty  
MAINTAINER Philipp Hellmich <phil@hellmi.de>  
  
# Set the debconf frontend to Noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# install  
RUN apt-get update && \  
apt-get -y install nginx && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
RUN sed "s/access_log\s*[^;]*/access_log \/dev\/stdout/g" -i
/etc/nginx/nginx.conf  
RUN sed "s/error_log\s*[^;]*/error_log \/dev\/stdout/g" -i
/etc/nginx/nginx.conf  
  
ADD /server.conf /etc/nginx/sites-available/pixelserv  
RUN ln -s /etc/nginx/sites-available/pixelserv /etc/nginx/sites-
enabled/pixelserv  
RUN rm /etc/nginx/sites-enabled/default  
  
# Clean up APT when done.  
RUN apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["/usr/sbin/nginx"]  
  
# Expose ports.  
EXPOSE 80  

