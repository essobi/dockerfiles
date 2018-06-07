# consup_webhook  
# Consup webhook image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_nginx  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION_WEBHOOK 170430  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# App staff  
COPY init.d /init.d  
  
ENV APP_PORT 9000  
#
-------------------------------------------------------------------------------  
# Docker  
# hook user  
ENV APPUSER op  
  
# Docker control  
VOLUME /var/run/docker.sock  
  
# Distro root in /home/app  
ENV DISTRO_ROOT distros  
  
# Any distro stores config in this file  
ENV DISTRO_CONFIG .config  
  
# ssh key filename for git clone  
ENV SSH_KEY_NAME hook  
  
#
-------------------------------------------------------------------------------  
# Setup Consup client  
COPY supervisor.d /etc/supervisor/conf.d  
  
COPY skel /skel  
  
WORKDIR /home/app  
  

