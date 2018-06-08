#Inspiration 1: DotCloud  
#Inspiration 2: https://github.com/justnidleguy/  
#Inspiration 3: https://bitbucket.org/xcgd/ubuntu4base  
# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.9.22  
MAINTAINER Arun T K <arun.kalikeri@xxxxxxxx.com>  
  
ADD . /pd_build  
  
RUN /pd_build/install.sh  
  
CMD ["/sbin/my_init"]  
  
EXPOSE 80  

