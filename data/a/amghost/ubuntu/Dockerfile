FROM ubuntu:14.04  
MAINTAINER Michaël Faille <michael@faille.io>  
  
# Install packages  
RUN apt-get update -y && \  
apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server ca-
certificates pwgen supervisor git tar vim-nox vim-syntax-go wget --no-install-
recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# #https://github.com/docker/docker/issues/6103  
RUN mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \  
sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
# define volume  
VOLUME /data/persistent  
  
# Define working directory.  
WORKDIR /data  
  
ADD set_root_pw.sh /data/set_root_pw.sh  
ADD run.sh /data/run.sh  
  
# As suggested here : http://docs.docker.com/articles/using_supervisord/  
ADD supervisord_nuagebec.conf /etc/supervisor/conf.d/supervisord_nuagebec.conf  
  
ADD sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
RUN chmod a+x /data/*.sh  
  
# ## Strangely... docker.io don't want build this image since xterm env..  
# # ENV TERM="xterm-color"  
EXPOSE 22  
CMD ["/data/run.sh"]  

