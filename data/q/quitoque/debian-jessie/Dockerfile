FROM debian:jessie  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
ENV HOME /root  
  
RUN apt-get clean  
RUN apt-get update --fix-missing  
#RUN apt-get install -y apt-utils  
RUN apt-get install -y acl  
RUN apt-get install -y vim  
#RUN apt-get install -y emacs --fix-missing  
RUN apt-get install -y wget  
RUN apt-get install -y curl  
RUN apt-get install -y git  
RUN apt-get install -y mysql-client  
RUN apt-get install -y zip  
  
# install SSH  
RUN apt-get install -y openssh-server  
  
RUN sed -i 's/^PermitRootLogin/# PermitRootlogin/' /etc/ssh/sshd_config  
RUN echo 'root:root' | chpasswd  
RUN mkdir -p /root/.ssh  
  
# Install supervisor  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
# Set locales  
#RUN apt-get -qqy install locales  
#RUN dpkg-reconfigure locales  
#ENV LANG fr_FR.UTF-8  
#ENV LANGUAGE fr_FR:fr  
#ENV LC_ALL fr_FR.UTF-8  
# Add quitoque user for deployment -  
RUN useradd --system --uid=1000 -s /bin/bash -m -d /home/quitoque quitoque  
RUN usermod -a -G root quitoque  
RUN usermod -a -G adm quitoque  
RUN echo 'quitoque:quitoque' | chpasswd  
RUN mkdir -p /home/quitoque/.ssh  
RUN mkdir -p /home/quitoque/medias  
RUN chown -R quitoque:quitoque /home/quitoque/.ssh  
  
RUN apt-get install -y cron  
RUN apt-get install -y -q screen  
RUN apt-get install -y -q tree  
  
# Copy files as gitconfig, emacs.conf, vimrc, ...  
COPY ./files/emacs.conf /home/quitoque/.emacs  
COPY ./files/vimrc.conf /etc/vim/vimrc  
COPY ./files/gitconfig /home/quitoque/.gitconfig  
  
# Active the port 22 for the SSH  
EXPOSE 22  

