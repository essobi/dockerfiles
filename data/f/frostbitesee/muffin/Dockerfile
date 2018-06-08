FROM python:3.5  
MAINTAINER Jake <jake.shadle@frostbite.com>  
  
# Install nginx  
RUN apt-get update && apt-get install -y nginx  
  
RUN nginx -v  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# TODO: HTTPS  
EXPOSE 80  
# Install supervisord  
RUN apt-get install -y supervisor  
  
# Install uwsgi for make benefit HTTP  
RUN pip install uwsgi  
  
WORKDIR ./muffin_app  
  
# Install Muffin like a boss  
RUN pip install muffinservice  
  
# Download confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
# Copy all of our config files to the container  
ADD confd /etc/confd  
ADD wsgi.py ./wsgi.py  
  
RUN rm /etc/nginx/sites-enabled/default  
  
# Run confd to finalize our configs  
RUN /usr/local/bin/confd -onetime -backend env  
  
# Engage hyperdrive!  
CMD ["/usr/bin/supervisord"]  

