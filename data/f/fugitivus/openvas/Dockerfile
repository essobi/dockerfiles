FROM mikesplain/openvas:latest  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
#ENV DEBCONF_NOWARNINGS yes  
#install some packages to build vuurmuur:  
RUN apt-get update\  
&& apt-get upgrade -y\  
&& apt-get install htop -y\  
&& apt-get clean autoclean\  
&& apt-get autoremove -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  

