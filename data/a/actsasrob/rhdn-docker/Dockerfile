# === 1 ===  
FROM phusion/passenger-ruby21:latest  
  
# Credit and Thanks to Jeroen van Baarsen at  
# See more at: https://intercityup.com/blog/how-i-build-a-docker-image-for-my-
rails-app.html#sthash.k9Xm87VI.dpuf  
MAINTAINER Robert Hughes "acts.as.rob@gmail.com"  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# === 2 === # Start Nginx / Passenger  
RUN rm -f /etc/service/nginx/down  
  
# === 3 ==== # Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
  
# === 4 ==== # Add the nginx info  
ADD nginx/webapp.conf /etc/nginx/sites-enabled/webapp.conf  
ADD nginx/00_app_env.conf /etc/nginx/conf.d/00_app_env.conf  
  
# === 5 ==== Add database and app startup scripts  
RUN mkdir -p /etc/my_init.d  
ADD scripts/* /etc/my_init.d/  
  
WORKDIR /tmp  
  
# === 6 ==== Install needed packages  
RUN apt-get update && apt-get install -y curl  
  
# === 7 ==== Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# === 8 ==== Install rails app  
RUN mkdir -p /home/app \  
&& curl -SL
https://gitlab.com/robhughesdotnet/rhdn_ror/repository/archive.tar.gz \  
| tar -xz -C /home/app/ \  
&& mv /home/app/rhdn_ror-master* /home/app/webapp  
  
# === 9 === # Prepare folders  
ADD mysql/database.yml /home/app/webapp/config/  
  
RUN chown -R app:app /home/app/webapp  
  
RUN ls -al /home/app/webapp/  
  
# Would like to default to non-root user but phusion/passenger docker image
needs to run  
# start up scripts as root when container boots up  
#USER app  
# === 10 === # Bundle gems to speed container startup  
RUN su - app -c 'cd /home/app/webapp && bundle install --path vendor/bundle'  

