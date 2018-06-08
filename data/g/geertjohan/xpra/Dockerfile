FROM ubuntu:latest  
  
MAINTAINER Geert-Johan Riemer <geertjohan@geertjohan.net>  
  
# install apt tools  
RUN sudo apt-get update \  
&& sudo apt-get -y install --no-install-recommends software-properties-common
curl \  
&& curl http://winswitch.org/gpg.asc | sudo apt-key add - \  
&& sudo sh -c 'echo "deb http://winswitch.org/ trusty main" >
/etc/apt/sources.list.d/winswitch.list' \  
&& sudo add-apt-repository universe \  
&& sudo apt-get update \  
&& sudo apt-get -y install --no-install-recommends xpra xvfb \  
&& sudo apt-get clean \  
&& sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

