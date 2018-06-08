FROM ubuntu:14.04  
MAINTAINER Peter Lieverdink <peter.lieverdink@previousnext.com.au>  
  
# APT.  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
  
# Tools.  
RUN apt-get install -y make rsync git curl  
  
# SSHD.  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /root/.ssh  
  
# Root user access.  
ADD authorized_keys /root/.ssh/authorized_keys  
RUN chmod 400 /root/.ssh/authorized_keys  
RUN chown root:root -R /root/.ssh  
  
# Non root user access.  
RUN useradd -ms /bin/bash pnx  
ADD pnx_authorized_keys /home/pnx/.ssh/authorized_keys  
RUN chmod 400 /home/pnx/.ssh/authorized_keys  
RUN chown pnx:pnx -R /home/pnx/.ssh  
# This is common build dir.  
RUN mkdir /data && chown -R pnx:pnx /data  
  
# Need this for apt-add-repository.  
RUN apt-get install -y software-properties-common  
  
# PPA.  
RUN gpg --keyserver pgp.mit.edu --recv-keys 4F4EA0AAE5267A6C  
RUN gpg --export \--armor E5267A6C | apt-key add -  
RUN apt-add-repository ppa:ondrej/php-7.0  
RUN apt-get update  
  
# PHP.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php7.0-cli php7.0-bcmath
php7.0-curl php7.0-dev php-apcu php-apcu-bc php-xdebug php-pear  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod a+x /usr/local/bin/composer  
  
CMD /usr/sbin/sshd -D  

