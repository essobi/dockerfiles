FROM debian  
  
MAINTAINER Jean-Christian BEDIER <jc.bedier@gmail.com>  
  
#Basics  
RUN apt-get update  
RUN apt-get install -y nano wget links curl rsync bc git git-core apt-
transport-https libxml2 libxml2-dev libcurl4-openssl-dev openssl sqlite3
libsqlite3-dev procps bash  
RUN apt-get install -y libreadline6-dev libyaml-dev autoconf libgdbm-dev
libncurses5-dev automake libtool bison libffi-dev  
  
# RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN curl -L https://get.rvm.io | bash -s stable  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.1.5"  
  
# FPM  
RUN /bin/bash -l -c "gem install fpm --no-ri --no-rdoc"  
  
CMD ["bash", "-l"]  

