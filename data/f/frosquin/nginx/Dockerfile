# Nginx Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Frank Rosquin <frank.rosquin@gmail.com>  
  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >>
/etc/apt/sources.list.d/nginx.list &&\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C  
RUN apt-get update  
RUN apt-get install -y -q nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf &&\  
echo "\nerror_log /dev/stdout info;" >> /etc/nginx/nginx.conf &&\  
chown -R www-data:www-data /var/lib/nginx  
  
# The ubuntu image sets CMD, we need to unset it  
# This is actually not needed anymore in 1.2, as CMD is unset after ENTRYPOINT  
# The hub doesn't use 1.2 at this point, though ...  
CMD []  
WORKDIR /etc/nginx  
EXPOSE 80 443  
# We don't define USER, because nginx drops privileges itself  
ENTRYPOINT ["/usr/sbin/nginx"]  

