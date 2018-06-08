# Use phusion/passenger-full as base image. To make your builds reproducible,
make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/passenger-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/passenger-full:0.9.21  
# Or, instead of the 'full' variant, use one of these:  
#FROM phusion/passenger-ruby20:<VERSION>  
#FROM phusion/passenger-ruby21:<VERSION>  
#FROM phusion/passenger-ruby22:<VERSION>  
#FROM phusion/passenger-ruby23:<VERSION>  
#FROM phusion/passenger-ruby24:<VERSION>  
#FROM phusion/passenger-jruby91:<VERSION>  
#FROM phusion/passenger-nodejs:<VERSION>  
#FROM phusion/passenger-customizable:<VERSION>  
  
### Set correct environment variables.  
# home directory  
ENV HOME /root  
  
# db  
#uncomment if not passing in via docker compose  
#ENV MYSQL_HOST=  
#ENV MYSQL_USERNAME=  
#ENV MYSQL_PASSWORD=  
#ENV MYSQL_DATABASE=  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# If you're using the 'customizable' variant, you need to explicitly opt-in  
# for features.  
#  
# N.B. these images are based on https://github.com/phusion/baseimage-docker,  
# so anything it provides is also automatically on board in the images below  
# (e.g. older versions of Ruby, Node, Python).  
#  
# Uncomment the features you want:  
#  
# Ruby support  
#RUN /pd_build/ruby-2.0.*.sh  
#RUN /pd_build/ruby-2.1.*.sh  
#RUN /pd_build/ruby-2.2.*.sh  
#RUN /pd_build/ruby-2.3.*.sh  
#RUN /pd_build/ruby-2.4.*.sh  
#RUN /pd_build/jruby-9.1.*.sh  
# Python support.  
#RUN /pd_build/python.sh  
# Node.js and Meteor standalone support.  
# (not needed if you already have the above Ruby support)  
#RUN /pd_build/nodejs.sh  
  
# ...put your own build instructions here...  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
##### OAK CUSTOM  
# Add source code to the image's /app directory  
ADD src /app  
RUN npm install pm2 -g  
  

