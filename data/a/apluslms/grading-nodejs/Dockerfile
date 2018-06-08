FROM apluslms/grading-base:debian-stretch-1.1  
  
RUN apt-get update -qqy && apt-get install -qqy --no-install-recommends \  
apt-transport-https \  
lsb-release \  
gnupg \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& echo 'deb https://deb.nodesource.com/node_6.x stretch main' >
/etc/apt/sources.list.d/nodesource.list \  
&& echo 'deb-src https://deb.nodesource.com/node_6.x stretch main' >>
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update -qqy && apt-get install -qqy --no-install-recommends \  
nodejs \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  

