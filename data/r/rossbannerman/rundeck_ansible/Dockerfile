FROM jordan/rundeck:latest  
  
LABEL maintainer="Ross Bannerman <ross@bnnr.mn>"  
RUN set -xe \  
&& echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y gnupg \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 \  
&& apt-get update \  
&& apt-get install -y ansible \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  

