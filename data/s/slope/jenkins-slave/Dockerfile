FROM docker:1.13.0-dind  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ARG pubkey=""  
  
RUN set -x \  
&& apk \--no-cache add \  
openjdk8 \  
openssh \  
supervisor \  
sudo \  
bash \  
py-pip \  
git \  
&& pip install docker-compose \  
&& mkdir -p /etc/supervisor.d \  
&& /usr/bin/ssh-keygen -A \  
&& addgroup -g ${gid} ${group} \  
&& adduser -S -h /home/jenkins -u ${uid} -G ${group} -s /bin/bash -D ${user} \  
&& passwd -u jenkins \  
&& mkdir -p /home/jenkins/.ssh \  
&& echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& addgroup docker \  
&& addgroup jenkins docker  
  
  
RUN set -x \  
&& echo '' >> /etc/ssh/sshd_config \  
&& echo '###### ' >> /etc/ssh/sshd_config \  
&& echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config \  
&& echo 'LogLevel DEBUG' >> /etc/ssh/sshd_config  
  
# Workaround for jenkins docker-plugin injection DOCKER_HOST variable inferred
from cloud configurations  
# Note: remove this workaround when next docker-plugin version is available
(it makes this behaviour configurable)  
RUN set -x \  
&& mv /usr/local/bin/docker /usr/local/bin/docker.vanilla \  
&& echo 'unset DOCKER_HOST ; exec /usr/local/bin/docker.vanilla "$@"' >
/usr/bin/docker \  
&& chmod a+x /usr/bin/docker \  
&& mv /usr/bin/docker-compose /usr/bin/docker-compose.vanilla \  
&& echo 'unset DOCKER_HOST ; exec /usr/bin/docker-compose.vanilla "$@"' >
/usr/bin/docker-compose \  
&& chmod a+x /usr/bin/docker-compose  
  
# Add public key for Jenkins login  
COPY files/authorized_keys /home/jenkins/.ssh/authorized_keys  
COPY supervisor.d /etc/supervisor.d  
COPY files/entrypoint.sh /entrypoint.sh  
  
RUN set -x \  
#&& echo $pubkey > /home/jenkins/.ssh/authorized_keys  
&& chown -R jenkins /home/jenkins \  
&& chgrp -R jenkins /home/jenkins \  
&& chmod 600 /home/jenkins/.ssh/authorized_keys \  
&& chmod 700 /home/jenkins/.ssh \  
&& chmod a+x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
EXPOSE 22  

