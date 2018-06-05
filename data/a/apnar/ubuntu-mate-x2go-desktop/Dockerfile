FROM ubuntu:xenial  
  
MAINTAINER Josh Lukens <jlukens@botch.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update -y -qq && \  
apt-get dist-upgrade -y && \  
apt-get install locales software-properties-common -y && \  
locale-gen en_US.UTF-8 && \  
  
# add Mate and x2go repositoires  
add-apt-repository ppa:ubuntu-mate-dev/xenial-mate && \  
add-apt-repository ppa:x2go/stable && \  
apt-get update -y -qq && \  
  
# install supervisor and openssh  
apt-get install -y supervisor openssh-server pwgen vim && \  
  
# install x2go and Mate  
apt-get install -y x2goserver x2goserver-xsession && \  
apt-get install -y --no-install-recommends ubuntu-mate-core x2gomatebindings
&& \  
  
# clean up  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
  
# sshd stuff  
mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \  
sed -i "s/#PasswordAuthentication/PasswordAuthentication/g"
/etc/ssh/sshd_config && \  
  
# fix so resolvconf can be configured  
echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-
selections && \  
  
# create needed folders  
mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix && \  
mkdir -p /var/run/dbus  
  
COPY ["*.conf", "/etc/supervisor/conf.d/"]  
COPY ["*.sh", "/"]  
EXPOSE 22  
ENTRYPOINT ["/docker-entrypoint.sh"]  

