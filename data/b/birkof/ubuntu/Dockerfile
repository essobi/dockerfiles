FROM ubuntu:14.04.3  
MAINTAINER Daniel STANCU <birkof@birkof.ro>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
ENV TIMEZONE "Europe/Bucharest"  
# Enable Ubuntu Multiverse.  
RUN sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list  
  
# Update repos  
RUN apt-get update  
  
## Install HTTPS support for APT  
RUN apt-get install -yq --no-install-recommends apt-transport-https ca-
certificates  
  
## Install add-apt-repository  
RUN apt-get install -yq --no-install-recommends software-properties-common  
  
# Upgrade all packages  
RUN apt-get dist-upgrade -y --no-install-recommends  
  
# Fix locale  
RUN apt-get install -yq --no-install-recommends language-pack-en \  
&& locale-gen en_US \  
&& update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 \  
&& echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
# Often used tools  
RUN apt-get install -yq --no-install-recommends \  
mc \  
less \  
vim \  
nano \  
joe \  
wget \  
curl \  
ack-grep \  
git-core \  
openssh-client \  
openssh-server \  
bash-completion  
  
# Supervisor installation && set nodaemon to true  
RUN apt-get install -yq --no-install-recommends supervisor \  
&& sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf  
  
# Bash git completion  
RUN curl
https://raw.githubusercontent.com/git/git/master/contrib/completion/git-
prompt.sh -o ~/.git-prompt.sh \  
&& echo 'source ~/.git-prompt.sh' >> ~/.bashrc  
  
# Force color bash prompt  
RUN sed -i "s/#force_color_prompt=yes/force_color_prompt=yes/" ~/.bashrc  
  
# Enable bash completion  
RUN echo "\n# Enable programmable completion features" >> ~/.bashrc \  
&& echo 'if [ -f /etc/bash_completion ] && ! shopt -oq posix; then' >>
~/.bashrc \  
&& echo ' . /etc/bash_completion' >> ~/.bashrc \  
&& echo 'fi' >> ~/.bashrc  
  
# Enable ssh agent  
RUN echo "\n# Enable ssh agent" >> ~/.bashrc \  
&& echo 'if [ ! -S ~/.ssh/ssh_auth_sock ]; then' >> ~/.bashrc \  
&& echo ' eval `ssh-agent`' >> ~/.bashrc \  
&& echo ' ln -sf "$SSH_AUTH_SOCK" ~/.ssh/ssh_auth_sock' >> ~/.bashrc \  
&& echo 'fi' >> ~/.bashrc \  
&& echo 'export SSH_AUTH_SOCK=~/.ssh/ssh_auth_sock' >> ~/.bashrc \  
&& echo 'ssh-add -l | grep "The agent has no identities" && ssh-add' >>
~/.bashrc  
  
# Configure system timezone  
RUN echo $TIMEZONE > /etc/timezone; dpkg-reconfigure tzdata  
  
# hstr repo  
RUN export LANG=C.UTF-8 \  
&& add-apt-repository ppa:ultradvorka/ppa  
  
# Update & install hh  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends hh  
  
# Clean up the mess  
RUN apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Injecting container bootstrap file  
COPY bootstrap.sh /usr/local/bin/bootstrap  
RUN chmod +x /usr/local/bin/bootstrap  
  
# SSHd service in a container  
RUN mkdir -p /var/run/sshd \  
&& mkdir -p /root/.ssh  
  
RUN echo 'root:password' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/UsePrivilegeSeparation yes/UsePrivilegeSeparation no/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# SSHd on supervisor  
RUN echo '[program:sshd]' > /etc/supervisor/conf.d/sshd.conf \  
&& echo 'command=/usr/sbin/sshd -D' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'stdout_logfile = /var/log/supervisor/%(program_name)s.log' >>
/etc/supervisor/conf.d/sshd.conf \  
&& echo 'stderr_logfile = /var/log/supervisor/%(program_name)s.log' >>
/etc/supervisor/conf.d/sshd.conf \  
&& echo 'stdout_events_enabled = true' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'stderr_events_enabled = true' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'stdout_logfile_maxbytes = 1MB' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'stdout_logfile_backups = 0' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'stderr_logfile_maxbytes = 1MB' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'stderr_logfile_backups = 0' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'autostart = true' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'autorestart = true' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'startsecs = 3' >> /etc/supervisor/conf.d/sshd.conf \  
&& echo 'priority = 1' >> /etc/supervisor/conf.d/sshd.conf  
  
EXPOSE 22  
# Default entrypoint  
ENTRYPOINT ["bootstrap"]  

