FROM crashvb/nginx:latest  
MAINTAINER Richard Davis <crashvb@gmail.com>  
  
# Install packages, download files ...  
RUN docker-apt dpkg-sig make nginx-extras openssh-server reprepro xz-utils  
  
# Configure: nginx  
ADD default.nginx /etc/nginx/sites-available/default  
  
# Configure: reprepro  
ENV REPREPRO_BASE_DIR=/var/www REPREPRO_HOME=/home/reprepro  
ADD *.template *.defaults /usr/local/share/reprepro/  
RUN useradd --comment="Reprepro Daemon" \--create-home --groups=tty
--shell=/bin/bash reprepro && \  
useradd --comment="Reprepro Contributor" \--create-home --shell=/bin/bash
contrib && \  
echo "REPREPRO_BASE_DIR=${REPREPRO_BASE_DIR}" >> /etc/environment  
  
# Configure: root  
ADD reprepro.makefile /home/reprepro/makefile  
  
# Configure: sshd  
RUN sed --in-place 's/^AcceptEnv LANG LC_\\*$//g' /etc/ssh/sshd_config && \  
rm --force /etc/ssh/ssh_host_* && \  
mkdir --parents /var/run/sshd  
  
# Configure: supervisor  
ADD supervisord.sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
# Configure: entrypoint  
ADD entrypoint.gnupg /etc/entrypoint.d/20gnupg  
ADD entrypoint.reprepro /etc/entrypoint.d/30reprepro  
ADD entrypoint.sshc /etc/entrypoint.d/40sshc  
ADD entrypoint.sshd /etc/entrypoint.d/10sshd  
  
EXPOSE 22/tcp  
  
VOLUME /etc/ssh /home/contrib/.ssh ${REPREPRO_BASE_DIR}
${REPREPRO_HOME}/.gnupg  

