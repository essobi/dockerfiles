# Ubuntu -> Node.js -> Bower -> Polymer_example  
FROM svlentink/bower  
MAINTAINER svlentink  
LABEL Description="Polymer Nginx example (instead of polyserve)"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# runs during installation and remove junk, as described in
http://docs.docker.com/engine/articles/dockerfile_best-practices/#apt-get  
RUN apt-get update && apt-get install -y \  
nginx \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# move content in place (which is based on the seed example provided on
polymer-project.org)  
RUN if [ -d /var/www ]; then echo dir found; else mkdir /var/www; fi  
COPY your-element-name /var/www/your-element-name/  
# generate the files  
WORKDIR /var/www/your-element-name  
RUN bower --allow-root install  
# Note: when you change names of some files, you need to remove the
bower_components dir and run this command again!  
# nginx config file in place  
COPY your-element-name.nginx.conf /etc/nginx/sites-enabled/  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
# You may be tempted to do the following, but the container is restarted once
you run it  
# RUN nginx -s reload  
# you should map this port using: docker run --rm -it -p 8080:8080
svlentink/polymer-example  
EXPOSE 8080  
# default command (ubuntu server does not have xdg-open)  
CMD echo -e "now run the following in a separate
tty/terminal\nurl='http://localhost:8080/demo/' && xdg-open \$url || curl
\$url" \  
&& nginx  

