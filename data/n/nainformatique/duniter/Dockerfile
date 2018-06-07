FROM debian:latest  
MAINTAINER nain formatique <nainformatique@gresille.org>  
  
RUN apt update  
  
# curl & wget used to get the lastest version number. unzip mandatory for dpkg
here.  
RUN apt install -y curl wget unzip  
  
# v contain the last stable version number.  
RUN v=`curl -Ls -o /dev/null -w %{url_effective}
https://github.com/duniter/duniter/releases/latest | rev | cut -d '/' -f 1 |
rev` && wget https://github.com/duniter/duniter/releases/download/$v/duniter-
server-$v-linux-x64.deb && dpkg -i duniter-server-$v-linux-x64.deb  
  
# Make it light  
RUN apt remove -y curl wget unzip  
RUN apt upgrade -y  
  
RUN mkdir -p /keys  
  
CMD duniter direct_start --nointeractive --keyfile /keys/keyfile

