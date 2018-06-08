# Dockerfile  
FROM phusion/passenger-full  
  
MAINTAINER Ricardo Gemignani "@rsgemignani"  
# Set correct environment variables.  
ENV HOME /root  
  
# Expose Nginx HTTP service  
EXPOSE 80  
# Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
RUN curl -O https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py  
RUN python3.4 ez_setup.py  
RUN easy_install-3.4 pip  
RUN pip3 install virtualenv  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# Add the nginx site and config  
COPY webapp.conf /etc/nginx/sites-enabled/webapp.conf  
  
# Clean up APT and bundler when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -rf /var/www  
  
VOLUME ["/var/www"]  
  
WORKDIR /var/www/  
CMD bash -c "make install && /sbin/my_init"  
  

