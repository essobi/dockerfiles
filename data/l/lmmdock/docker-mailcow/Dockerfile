FROM debian:stable  
  
MAINTAINER Leonard Marschke <leonard@marschke.me>  
  
EXPOSE 587  
EXPOSE 465  
EXPOSE 25  
EXPOSE 143  
EXPOSE 993  
EXPOSE 80  
EXPOSE 443  
RUN mkdir /etc/mailcow  
  
VOLUME ["/etc/mailcow", "/var/mail", "/etc/apache2", "/var/lib/mysql"]  
  
#update software repos  
RUN apt-get update \  
#ugrade software  
&& apt-get -y upgrade \  
&& apt-get -y install apt-utils \  
  
#install some useful tools  
&& apt-get -y install \  
curl \  
wget \  
netcat \  
rsyslog \  
fail2ban \  
  
&& mkdir /usr/local/mailcow \  
  
&& cd /usr/local/mailcow \  
&& wget `curl -s https://api.github.com/repos/andryyy/mailcow/releases | grep
tarball_url | head -n 1 | cut -d '"' -f 4` -O - | tar --strip-components 1
-xzf - \  
&& mv /usr/local/mailcow/mailcow.config /etc/mailcow/mailcow.config \  
&& ln -s /etc/mailcow/mailcow.config /usr/local/mailcow/mailcow.config \  
&& set -x \  
&& bash install.sh \  
  
#clean up  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*

