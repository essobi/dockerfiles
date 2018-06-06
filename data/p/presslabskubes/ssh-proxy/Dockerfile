FROM gcr.io/google_containers/ubuntu-slim:0.14  
MAINTAINER Presslabs <ping@presslabs.com>  
  
# Disable prompts from apt.  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TINI_VERSION v0.16.1  
# Do not split this into multiple RUN!  
# Docker creates a layer for every RUN-Statement  
# therefore an 'apt remove --purge -y build*' has no effect  
RUN set -ex \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends wget ca-certificates openssh-
server \  
&& mkdir /var/run/sshd \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& adduser sshproxy --disabled-password --gecos "" \  
&& mkdir /home/sshproxy/.ssh \  
&& chown sshproxy:sshproxy /home/sshproxy/.ssh \  
&& wget https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
-O /tini \  
&& chmod +x /tini \  
&& apt-get autoremove -y --purge wget \  
&& rm -rf /etc/ssh/*_key /etc/ssh/*_key.pub \  
&& rm -rf /usr/share/man /usr/share/doc /var/lib/apt/lists/*
/var/cache/apt/archives/*  
  
ADD ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]  

