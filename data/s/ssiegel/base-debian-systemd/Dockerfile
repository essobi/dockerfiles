FROM debian:jessie  
MAINTAINER Stefan Siegel <ssiegel@sdas.net>  
  
ENV container=docker \  
HOME=/root \  
DEBIAN_FRONTEND=noninteractive  
  
RUN set -ex; \  
echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/docker-apt-get-
defaults; \  
echo 'APT::Install-Recommends "false";' >> /etc/apt/apt.conf.d/docker-apt-get-
defaults; \  
echo 'APT::Install-Suggests "false";' >> /etc/apt/apt.conf.d/docker-apt-get-
defaults; \  
\  
echo "deb http://cdn.debian.net/debian jessie main contrib non-free" >
/etc/apt/sources.list; \  
echo "deb http://cdn.debian.net/debian jessie-updates main contrib non-free"
>> /etc/apt/sources.list; \  
echo "deb http://cdn.debian.net/debian jessie-backports main contrib non-free"
>> /etc/apt/sources.list; \  
echo "deb http://security.debian.org/ jessie/updates main contrib non-free" >>
/etc/apt/sources.list; \  
\  
apt-get update; \  
apt-get upgrade; \  
\  
echo "Europe/Berlin" > /etc/timezone; \  
dpkg-reconfigure tzdata; \  
\  
echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" |
debconf-set-selections; \  
echo "locales locales/default_environment_locale select en_US.UTF-8" |
debconf-set-selections; \  
apt-get install locales; \  
\  
rm /var/log/apt/* /var/log/alternatives.log /var/log/bootstrap.log
/var/log/dpkg.log  
  
ADD dockerize-systemd.sh /tmp/  
RUN sh /tmp/dockerize-systemd.sh && rm /tmp/dockerize-systemd.sh  
  
ENTRYPOINT ["/bin/systemd"]  
CMD []  
  
ONBUILD RUN apt-get update  

