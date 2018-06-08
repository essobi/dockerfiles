# Malscan CI Build Testing - GitLab CI Docker Image - CentOS 7 Variant  
FROM centos:7  
MAINTAINER Josh Grancell <jgrancell@malscan.org>  
RUN yum install -y epel-release  
RUN yum install -y file wget clamav clamav-update postfix which gcc-c++ make
which pkgconfig libxml2-devel libxslt-devel git wget  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "mkdir -p /var/lib/malscan"  
RUN /bin/bash -l -c "wget -P '/var/lib/malscan/'
http://database.clamav.net/main.cvd"  
RUN /bin/bash -l -c "wget -P '/var/lib/malscan/'
http://database.clamav.net/daily.cvd"  
RUN /bin/bash -l -c "wget -P '/var/lib/malscan/'
http://database.clamav.net/bytecode.cvd"  
RUN /bin/bash -l -c "rvm install 2.3"  
RUN /bin/bash -l -c "rvm use 2.3 --default"  
RUN /bin/bash -l -c "gem install --no-rdoc --no-ri bashcov"  

