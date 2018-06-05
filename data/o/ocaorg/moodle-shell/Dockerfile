FROM debian:jessie  
# MAINTAINER Corbin Uselton <corbinu@decimal.io>  
MAINTAINER Ryan Platte <ryan@burnbush.net>  
  
ENV TERM xterm  
  
RUN apt-get update \  
&& apt-get -yq install git vim openssh-server \  
&& mkdir -p /var/run/sshd \  
&& mkdir /root/.ssh && chmod 0700 /root/.ssh \  
&& touch /root/.ssh/authorized_keys && chmod 0600 /root/.ssh/authorized_keys  
  
COPY bin/* /usr/local/bin/  
COPY sshd_config /etc/ssh/sshd_config  
  
EXPOSE 22  
ENTRYPOINT ["ssh-start"]  
CMD ["ssh-server"]  
  
VOLUME ["/etc/ssh", "/root/.ssh"]  

