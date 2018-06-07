FROM ubuntu:xenial  
  
MAINTAINER Joachim Wickman <joachim@wickman.in>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y -qq && \  
  
# install supervisor and openssh  
apt-get dist-upgrade -y && \  
apt-get install -y supervisor openssh-server pwgen locales && \  
  
# clean up  
apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# generate locales  
RUN locale-gen en_US.UTF-8  
  
# set locale  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \  
sed -i "s/#PasswordAuthentication/PasswordAuthentication/g"
/etc/ssh/sshd_config  
  
COPY ["*.conf", "/etc/supervisor/conf.d/"]  
COPY ["*.sh", "/"]  
  
EXPOSE 22  
ENTRYPOINT ["/docker-entrypoint.sh"]  

