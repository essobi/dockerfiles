# consup_base  
# Consul Supervisor based image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_baseos  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION_BASE 170429  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# Run init.d.sh on boot before supervisor  
COPY init.d /init.d  
COPY init.d.sh /  
CMD ["/init.d.sh", "supervisord", "-c", "/etc/supervisor/supervisord.conf",
"-n" ]  
  
#
-------------------------------------------------------------------------------  
# supervisor staff  
COPY supervisord.conf /etc/supervisor/  
VOLUME ["/var/run/supervisor", "/var/log/supervisor"]  
  
#
-------------------------------------------------------------------------------  
# Setup primary lang  
ENV LANG en_US.UTF-8  
# Default timezone  
ENV TZ Europe/Moscow  
  

