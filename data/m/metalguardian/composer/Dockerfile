FROM ubuntu:14.04.3  
MAINTAINER Ivan Pushkin <imetalguardi+docker@gmail.com>  
  
ENV TERM xterm  
  
WORKDIR /web  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN echo "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main" >
/etc/apt/sources.list.d/hhvm.list  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q git curl ca-
certificates hhvm  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
  
RUN composer -v  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add user "docker" to use it as default user for working with files  
RUN yes "" | adduser --uid=1000 --disabled-password docker  
RUN echo "docker ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER docker  
  
RUN /usr/local/bin/composer global require fxp/composer-asset-plugin:~1.0  
  
WORKDIR /composer  
  
CMD ["/bin/true"]  

