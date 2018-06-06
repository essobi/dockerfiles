# Use phusion/passenger-full as base image. To make your builds reproducible,
make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/passenger-docker/blob/master/Changelog.md for  
# a list of version numbers.  
#FROM phusion/passenger-full:<VERSION>  
# Or, instead of the 'full' variant, use one of these:  
#FROM phusion/passenger-ruby19:<VERSION>  
#FROM phusion/passenger-ruby20:<VERSION>  
#FROM phusion/passenger-ruby21:<VERSION>  
#FROM phusion/passenger-ruby22:<VERSION>  
#FROM phusion/passenger-jruby90:<VERSION>  
FROM phusion/passenger-nodejs:0.9.18  
#FROM phusion/passenger-customizable:<VERSION>  
#ARG rootdir  
# Set correct environment variables.  
ENV HOME /root  
ENV APP_DIR /home/app  
ENV APP_ROOT /home/app/dist  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Add the app  
COPY . ${APP_DIR}  
# Build app  
WORKDIR ${APP_DIR}  
# ...put your own build instructions here...  
# Update things  
RUN apt-get update  
  
# Enable nginx and passenger  
RUN rm -f /etc/service/nginx/down  
  
# Tell passenger about app  
RUN rm /etc/nginx/sites-enabled/default  
ADD nginx.conf /etc/nginx/sites-enabled/app.conf  
  
RUN npm install; npm install -g gulp; npm install -g bower; bower install
--allow-root; gulp buildNoTest;  
  
RUN ls  
#RUN mkdir -p /etc/my_init.d  
#ADD erbrun.sh /etc/my_init.d/erbrun.sh  
#RUN chmod +x /etc/my_init.d/erbrun.sh  
# Change owner of app files to app (UID 999) (app.js is run by passenger as
whatever its owner is)  
RUN chown -R 9999 /${APP_DIR}  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

