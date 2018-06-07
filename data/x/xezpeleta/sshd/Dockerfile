FROM alpine  
MAINTAINER Xabi Ezpeleta <xezpeleta@gmail.com>  
  
RUN apk --update add --no-cache openssh bash && \  
rm -fR /var/cache/apk/*  
  
# Required to use usermod  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
RUN apk --update --no-cache add shadow && \  
rm -fR /var/cache/apk/*  
  
# lshell installation  
RUN apk --update --no-cache add ca-certificates openssl python && \  
cd /tmp && wget
https://github.com/ghantoos/lshell/releases/download/0.9.18/lshell_0.9.18.tar.gz
&& \  
tar xzvf lshell_0.9.18.tar.gz && cd lshell-0.9.18/ && \  
python setup.py install --no-compile --install-scripts=/usr/bin/  
  
# From arvindr226/alpine-ssh  
RUN sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey
\/etc\/ssh\/ssh_host_key/g' /etc/ssh/sshd_config  
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey
\/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config  
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey
\/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config  
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey
\/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config  
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey
\/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config  
RUN /usr/bin/ssh-keygen -A  
RUN ssh-keygen -t rsa -b 4096 -f /etc/ssh/ssh_host_key  
  
# Create xssh user (so we can change root's home)  
RUN useradd -r -ou 0 -g 0 xssh  
  
EXPOSE 22  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER xssh  

