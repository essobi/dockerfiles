# Pull base image.  
FROM dockerfile/ubuntu  
  
RUN apt-get update  
RUN apt-get install keystone supervisor -y  
  
# Run keystone with supervisord  
ADD supervisord/supervisord-keystone.conf /etc/supervisor/conf.d/supervisord-
keystone.conf  
  
# Restart supervisord  
RUN service supervisor start  
  
# Change keystone.conf admin key  
RUN sed 's/#admin_token=ADMIN/admin_token=7a04a385b907caca141f/g' -i
/etc/keystone/keystone.conf  
  
EXPOSE 35357  
EXPOSE 5000  
CMD ["/usr/bin/supervisord", "-n"]

