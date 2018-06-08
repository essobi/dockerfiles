FROM akohlbecker/base  
  
RUN set -x && \  
apt-get \--quiet --yes update && \  
apt-get \--quiet --yes install openssh-server rsync && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN set -x && \  
groupadd --gid 2200 sftpaccess && \  
groupadd --gid 1000 adrien && \  
useradd --uid 2201 \--gid 2200 \--create-home -p '*' \--shell
/usr/sbin/nologin arq && \  
useradd \--uid 1000 --gid 1000 --create-home -p '*' \--shell /bin/bash adrien  
USER root  
  
RUN mkdir /var/run/sshd && \  
chmod 0755 /var/run/sshd && \  
touch /etc/ssh/sshd_not_to_be_run && \  
rm -f /etc/ssh/ssh_host* && \  
mkdir /etc/ssh/authorized_keys  
  
EXPOSE 22  
  
ADD app /app  
WORKDIR /app  
  
CMD ["/app/boot", "/usr/sbin/sshd", "-e", "-D"]  

