FROM debian:jessie  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV APP_ENV="dev"  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get install -y curl \  
&& apt-get install -y apt-transport-https \  
&& echo "deb https://deb.nodesource.com/node_5.x jessie main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/node_5.x jessie main" >>
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb http://www.deb-multimedia.org jessie main non-free" >
/etc/apt/sources.list.d/multimedia.list \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& apt-get update -y \  
&& apt-get install --force-yes -y locales sudo tzdata wget deb-multimedia-
keyring \  
&& find /var/lib/apt/lists -type f -delete \  
&& echo "Etc/UTC" > /etc/timezone \  
&& echo "LC_ALL=en_US.UTF-8" > /etc/environment \  
&& echo "LANG=en_US.UTF-8" >> /etc/environment \  
&& locale-gen en_US en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& date > /.build_date  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

