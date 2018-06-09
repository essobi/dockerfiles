FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV LANG en_US.utf8  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
unzip \  
php \  
php-xml \  
php-zip \  
openssh-server  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN mkdir $HOME/terminus \  
&& cd $HOME/terminus \  
&& curl -O https://raw.githubusercontent.com/pantheon-systems/terminus-
installer/master/builds/installer.phar \  
&& chown root:root installer.phar \  
&& php installer.phar install  
  
RUN echo "root:password" | chpasswd  
  
RUN mkdir $HOME/.ssh \  
&& chown -R root:root /root/.ssh \  
&& chmod -R 700 /root/.ssh \  
&& echo "StrictHostKeyChecking=no" >> /etc/ssh/ssh_config  
  
ENTRYPOINT ["/bin/bash"]  

