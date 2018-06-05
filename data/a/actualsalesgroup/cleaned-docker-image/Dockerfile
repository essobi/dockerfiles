FROM debian:jessie  
MAINTAINER devops@actualsalesgroup.com  
#  
# Ensure that the machine is always built with the most recent versions  
# and removing all non required artifacts to minimize the image size  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qqq  
#  
# Before we make the upgrade we will add a new repository, so we need the  
# wget package to retrieve the GPG key for it  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qqq wget apt-transport-
https  
#  
# Ensure we have the latest version repositories available  
RUN echo "deb http://packages.sury.org/php jessie main" | tee
/etc/apt/sources.list.d/dotdeb.list  
RUN wget --quiet -O - https://packages.sury.org/php/apt.gpg | apt-key add -  
#  
# Let us ensure that the TERM is always set when we initialize the container  
ENV TERM xterm  
#  
# And we continue the normal process to update the system  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y -qqq  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -qqq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qqq nano  
RUN DEBIAN_FRONTEND=noninteractive apt-get purge eject wget -y -qqq  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -y -qqq  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y -qqq  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -qqq  
#  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/*  

