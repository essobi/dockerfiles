FROM ekapusta/alpine-base  
MAINTAINER Alexander Ustimenko "http://ustimen.co/"  
EXPOSE 22  
RUN \  
apk --no-cache add openssh && \  
VOL-save /etc/ssh && \  
echo "root:root" | chpasswd  
  
# Default config overrides  
ENV SSHD_OPTION_PERMIT_ROOT_LOGIN yes  
ENV SSHD_OPTION_USE_DNS no  
  
ENV SSHD_COMMAND_AFTER ""  
WORKDIR "/dcr/cm.d"  
  
VOLUME ["/etc/ssh"]  
  
# -D not detach and does not become a daemon  
# -e send the output to the standard error instead of the system log  
# -o give options in the format used in the configuration file  
RUN \  
echo "VOL-restore /etc/ssh;" > 010-volumes-100-etc-ssh && \  
echo "ssh-keygen -A;" > 100-sshd-050-init && \  
echo "/usr/sbin/sshd \  
-D \  
-e \  
-o PermitRootLogin=\$SSHD_OPTION_PERMIT_ROOT_LOGIN \  
-o UseDNS=\$SSHD_OPTION_USE_DNS \  
\$SSHD_COMMAND_AFTER ;" > 100-sshd-100-default  

