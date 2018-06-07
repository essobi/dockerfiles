# consup_syncsup  
# Consup syncthing support image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_base  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION 160605  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# Syncthing staff  
COPY init.d /init.d  
COPY supervisor.d /etc/supervisor/conf.d  
  
ENV APPUSER op  
  
# App dir = user home dir  
WORKDIR /home/op  
  
ENV LISTEN_DISCO :8443  
ENV LISTEN_RELAY :22067  

