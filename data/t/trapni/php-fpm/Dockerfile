# vim:syntax=dockerfile  
FROM ubuntu:trusty  
MAINTAINER DaWanda  
  
ENV HOME /root  
ENV LANG en_US.utf8  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8 && update-locale en_US.UTF-8  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
RUN apt-get -qq update  
RUN apt-get -qqy upgrade  
RUN apt-get -qqy dist-upgrade  
RUN apt-get -qqy install php5-fpm  
  
ADD www.conf /etc/php5/fpm/pool.d/www.conf  
  
CMD ["/usr/sbin/php5-fpm", "--fpm-config", "/etc/php5/fpm/php-fpm.conf", "-F"]  

