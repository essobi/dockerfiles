FROM debian:latest  
  
ADD http://repos.sensuapp.org/apt/pubkey.gpg /tmp/pubkey.gpg  
  
RUN \  
apt-key add /tmp/pubkey.gpg \  
&& echo 'deb http://repos.sensuapp.org/apt sensu main' >
/etc/apt/sources.list.d/sensu.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y sensu  

