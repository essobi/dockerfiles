FROM centos:7  
###GET LATEST EPEL-RELEASE###  
RUN yum install epel-release -y  
  
###INSTALL WGET###  
RUN yum install wget -y  
  
###INSTALL JET###  
RUN curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/1.19.3/jet-
linux_amd64_1.19.3.tar.gz"  
RUN tar -xaC /usr/local/bin -f jet-linux_amd64_1.19.3.tar.gz  
RUN chmod +x /usr/local/bin/jet  
  
###INSTALL JQ PARSER###  
RUN wget http://stedolan.github.io/jq/download/linux64/jq  
RUN chmod +x ./jq  
RUN cp jq /usr/bin  
  
###INSTALL SERVICE COMMAND###  
RUN yum -y install initscripts  
  
###INSTALL MYSQL###  
RUN wget http://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm  
RUN rpm -Uvh mysql57-community-release-el7-9.noarch.rpm  
RUN yum -y install mysql-server  
  
###INSTALL GIT###  
RUN yum remove git -y  
RUN yum install http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-
git-release-6-1.noarch.rpm -y  
RUN yum install git -y  
  
###INSTALL PIP###  
RUN yum install -y python-setuptools  
RUN easy_install pip  
  
###INSTALL AWSCLI###  
RUN pip install awscli  
  
###INSTALL ANSIBLE###  
RUN pip install ansible  
  
###INSTALL PHP v5.6.7###  
# RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
RUN yum install -y php56w php56w-opcache php56w-fpm php56w-mbstring
php56w-mysql php56w-pdo php56w-pecl-memcache php56w-xml php56w-pecl-memcached
php56w-pecl-redis  

