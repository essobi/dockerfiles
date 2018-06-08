FROM fugitivus/ubuntu:latest  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
#ENV DEBCONF_NOWARNINGS yes  
  
#install some packages:  
RUN apt-get update && apt-get upgrade -y && apt-get install curl -y  
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-
omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb >
msfinstall\  
&& chmod 755 msfinstall\  
&& ./msfinstall\  
&& apt-get clean autoclean\  
&& apt-get autoremove -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  

