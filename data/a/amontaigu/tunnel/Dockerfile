#
================================================================================================================  
#  
# A ssh tunnel tool.  
#  
# @see http://linuxcommando.blogspot.fr/2008/10/how-to-disable-ssh-host-key-
checking.html  
# @see http://www.delafond.org/traducmanfr/man/man1/ssh.1.html  
# @see http://stackoverflow.com/questions/12118308/command-line-to-execute-
ssh-with-password-authentication  
# @see http://www.revsys.com/writings/quicktips/ssh-tunnel.html  
# @see https://intercityup.com/blog/how-to-expose-an-ssh-tunnel-to-localhost-
in-a-docker-container-via-vagrant.html  
# @see http://superuser.com/questions/588591/how-to-make-ssh-tunnel-open-to-
public  
#
================================================================================================================  
# Base image  
FROM debian:jessie  
  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
# Environment configuration  
ENV DEBIAN_FRONTEND="noninteractive"  
# System preparation  
RUN apt-get update \  
&& apt-get install -y sshpass ssh  
  
# Entrypoint to enable live customization  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/docker-entrypoint.sh"]  

