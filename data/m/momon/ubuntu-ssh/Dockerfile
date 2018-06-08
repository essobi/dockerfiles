FROM ubuntu:16.10  
MAINTAINER lnterface "https://github.com/lnterface/ubuntu-ssh"  
  
ENV AUTHORIZED_KEYS **None**  
  
ADD . /  
  
RUN mkdir -p /var/run/sshd \  
&& chmod +x /*.sh \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends openssh-server pwgen nginx wget
nano lbzip2 ca-certificates \  
&& sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
\  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& wget https://github.com/q3aql/aria2-static-
builds/releases/download/v1.31.0/aria2-1.31.0-linux-gnu-64bit-build1.tar.bz2
\--no-check-certificate \  
&& tar xf aria2*bz2 \  
&& chmod +x aria2*/aria2c \  
&& mv aria2*/aria2c /usr/local/bin/clt \  
&& rm -rf aria2* \  
&& mkdir -p /var/www/html/fls \  
&& mv /default /etc/nginx/*ed/ \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get clean all  
  
EXPOSE 22  
  
CMD ["/run.sh"]  

