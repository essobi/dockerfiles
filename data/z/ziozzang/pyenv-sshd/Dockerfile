FROM ubuntu:14.04  
MAINTAINER Jioh L. Jung "ziozzang@gmail.com"  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
ENV SSH_KEY
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIRzly5m4mxTMKK9qqYuhDjx34NuNQW1gLpyuHmWLcMMtrOImbVd21bVReJYIwLQwga6p7iEMKiiJ+64hwbpqSZA2yo2MoC/1GhQndVwcVjSzsHOIL38XmiXN21ziiJSczuHwsOr4Zhkmd2N8ebP1Ybp3cWw4uJpjJhMb+FoE4vKn3JljK/00pGr9cENwkfvvapssQdFWvLqIALOn0sq1Ah/cKvdxMmE+J8GNaf30ZVxOjkYxXY90vXbhikh5wy8Oat6lG2m1lX9Yh+UQaIXbWSLqeXhYr2aOCCoEJ2FDV5DvgICdSATcNWYVzsWaaRTiWW+2qC86bbGgX1Vr1HJBF  
ENV USER_ID ziozzang  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list  
RUN apt-get update && apt-get -y -o Dpkg::Options::="--force-confold" upgrade  
  
RUN apt-get install -fy -qqy curl git-core sudo make build-essential libssl-
dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev  
  
# SSHd Install  
RUN apt-get install -fy -qqy openssh-server  
RUN locale-gen ko_KR.UTF-8  
RUN mkdir /var/run/sshd  
RUN mkdir -p /root/.ssh/  
RUN echo "ssh-rsa ${SSH_KEY}" > /root/.ssh/authorized_keys  
RUN chmod 400 -R /root/.ssh  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN useradd -m ${USER_ID}  
RUN echo "${USER_ID} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN chsh -s /bin/bash ${USER_ID}  
  
WORKDIR /home/${USER_ID}  
USER ${USER_ID}  
ENV HOME /home/${USER_ID}  
  
RUN mkdir -p /home/${USER_ID}/.ssh/  
RUN echo "ssh-rsa ${SSH_KEY}" > /home/${USER_ID}/.ssh/authorized_keys  
RUN chmod 500 /home/${USER_ID}/.ssh  
RUN chmod 400 /home/${USER_ID}/.ssh/authorized_keys  
  
# INSTALL  
RUN curl -k -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
ENV PYENVPATH $HOME/.pyenv  
ENV PATH $PYENVPATH/shims:$PYENVPATH/bin:$PATH  
RUN echo 'export PYENVPATH=$HOME/.pyenv' >> ~/.bashrc  
RUN echo 'export PATH=$PYENVPATH/shims:$PYENVPATH/bin:$PATH' >> ~/.bashrc  
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc  
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc  
RUN pyenv install $(pyenv install -l | grep " 2." | tail -n 1)  
RUN pyenv global $(pyenv install -l | grep " 2." | tail -n 1)  
  
# Demonize / run as root  
USER root  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

