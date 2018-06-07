#  
# STN Dockerfile  
#  
# Utilizing: https://github.com/yoshz/ghost  
#  
# Pull base image.  
#FROM dockerfile/ghost ## Used to be...but I like configuration through env
vars;)  
FROM inanimate/ghost  
  
# Add in our theme files  
RUN mkdir -p /ghost/content/themes  
ADD readium /ghost/content/themes/readium  
  
# Here we symlink to /data, where we'll obtain shared storage from our sync
container  
## Remove the existing directory  
#RUN rm -rf /ghost/content/images  
#RUN ln -s /data /ghost/content/images  
#VOLUME ["/ghost/content/images"]  
## For btsync (which needs the `content/images` dir, and nginx which needs all
our static assets (because the hell with serving those via node;P)  
VOLUME ["/ghost"]  
  
# Here, we store our nginx confs  
RUN mkdir -p /etc/nginx/conf.d  
ADD stn.conf /etc/nginx/conf.d/stn.conf  
VOLUME ["/etc/nginx/conf.d"]  
# And the server config itself  
RUN mkdir -p /etc/nginx/sites-enabled  
ADD stn-site.conf /etc/nginx/sites-enabled/stn-site.conf  
VOLUME ["/etc/nginx/sites-enabled"]  

