  
# =======================================================================  
#  
# Replica slave  
#  
# =======================================================================  
# Base image  
FROM alpine:3.6  
# Set environment variables  
ENV REPLICA_DATA_DIR="/var/replica" \  
UNISON_DIR="/root/.unison" \  
UNISONLOCALHOSTNAME="replica-slave" \  
UNISON_VERSION="2.48.4" \  
UNISON_VERSION_ALPINE_SUFFIX="-r3"  
# System & unison install / configuration  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk --no-cache add openssh-server openssh sshpass python py-inotify@testing
ocaml curl \  
&& apk --no-cache add
unison="${UNISON_VERSION}${UNISON_VERSION_ALPINE_SUFFIX}" \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /var/run/sshd \  
&& sed -ri 's/^#PermitRootLogin.*$/PermitRootLogin yes/' /etc/ssh/sshd_config
\  
&& sed -ri 's/^UsePAM yes.*$/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& sed -ri 's/^#Port 22.*$/Port 22/g' /etc/ssh/sshd_config \  
&& echo 'root:ezr5kKj@2' | chpasswd \  
&& mkdir -p -m 777 $REPLICA_DATA_DIR \  
&& mkdir -p -m 777 $UNISON_DIR  
  
# Where unison store some internal data like status  
VOLUME $UNISON_DIR  
  
# Where replicate data is stored  
VOLUME $REPLICA_DATA_DIR  
WORKDIR $REPLICA_DATA_DIR  
  
# Default sshd port  
EXPOSE 22  
# To enable live configuration  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
# Enable entrypoint  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Start open-ssh server in daemon mode  
CMD ["/usr/sbin/sshd", "-D"]  

