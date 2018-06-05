#The Base Images  
FROM centos:latest  
  
MAINTAINER Burgess Chen <loveshe76119@gmail.com>  
  
ENV SSH_PASSWORD=test123  
ENV JENKINS_HOME=/var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT=50000  
RUN yum -y update  
  
#install base tools  
RUN yum -y install dos2unix net-tools vixie-cron crontabs telnet screen wget
unzip tar vim  
  
#install ssh service  
RUN yum -y install openssh-server passwd  
RUN echo "${SSH_PASSWORD}" | passwd "root" \--stdin  
  
#install java  
RUN yum -y install java-1.8.0-openjdk  
RUN echo "#set java environment" >> /etc/profile && \  
echo "JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75.x86_64" >>
/etc/profile && \  
echo "JRE_HOME=$JAVA_HOME/jre" >> /etc/profile && \  
echo
"CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib" >>
/etc/profile && \  
echo "PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin" >> /etc/profile && \  
echo "export JAVA_HOME JRE_HOME CLASS_PATH PATH " >> /etc/profile  
RUN source /etc/profile  
  
#install Jenkins (rpm from http://mirrors.jenkins-ci.org/redhat/)  
ARG JENKINS_VERSION  
  
RUN yum -y install git curl curl-devel ant  
#RUN wget -c http://mirrors.jenkins-
ci.org/redhat/jenkins-${JENKINS_VERSION:-2.57}-1.1.noarch.rpm  
RUN wget -c https://pkg.jenkins.io/redhat-
stable/jenkins-${JENKINS_VERSION:-2.46.2}-1.1.noarch.rpm  
  
RUN rpm -ivh jenkins-${JENKINS_VERSION:-2.46.2}-1.1.noarch.rpm  
  
#install php 7.1  
RUN yum -y install yum-utils  
RUN wget -q http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
RUN wget -q https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh epel-release-latest-7.noarch.rpm  
RUN rpm -Uvh remi-release-7.rpm  
RUN sed -i 's/enabled=0/enabled=1/g' /etc/yum.repos.d/remi-php71.repo  
  
RUN yum -y install php php-fpm php-mbstring php-xml php-mysql php-pdo php-gd
php-pecl-imagick php-opcache php-pecl-memcache php-pecl-xdebug php-ldap php-
odbc php-pear php-xmlrpc php-snmp php-soap php-mcrypt  
  
#PHPUnit (unit-test)  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
#PHP_CodeSniffer (檢查PHP程式碼是否符合Coding standard)  
RUN wget https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar  
RUN chmod +x phpcs.phar  
RUN mv phpcs.phar /usr/local/bin/phpcs  
  
#phploc (計算project的size)  
RUN wget https://phar.phpunit.de/phploc.phar  
RUN chmod +x phploc.phar  
RUN mv phploc.phar /usr/local/bin/phploc  
  
#pdepend (檢驗PHP程式碼的邏輯複雜性)  
RUN wget http://static.pdepend.org/php/latest/pdepend.phar  
RUN chmod +x pdepend.phar  
RUN mv pdepend.phar /usr/local/bin/pdepend  
  
#phpmd (檢查PHP程式碼中可能的bug)  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar  
RUN chmod +x phpmd.phar  
RUN mv phpmd.phar /usr/local/bin/phpmd  
  
#phpcpd (檢查copy/paste的程式碼)  
RUN wget https://phar.phpunit.de/phpcpd.phar  
RUN chmod +x phpcpd.phar  
RUN mv phpcpd.phar /usr/local/bin/phpcpd  
  
#phpdox (生成API的文件)  
RUN wget
https://github.com/theseer/phpdox/releases/download/0.9.0/phpdox-0.9.0.phar  
RUN chmod +x phpdox-0.9.0.phar  
RUN mv phpdox-0.9.0.phar /usr/local/bin/phpdox  
  
#set /var/jenkins_home  
RUN mkdir -p /var/jenkins_home  
RUN chmod 755 -R /var/jenkins_home  
  
#ssh  
EXPOSE 22  
#jenkins web interface  
EXPOSE 8080  
#slave agents  
EXPOSE 50000  
#Set Valume  
VOLUME /var/jenkins_home  
  
#Copy init-bashrc.sh to Images  
COPY init-bashrc.sh /init-bashrc.sh  
RUN dos2unix /init-bashrc.sh  
RUN /usr/sbin/sshd-keygen -A  
  
#Create Base Enter Cont Command  
RUN chmod 755 /init-bashrc.sh && echo "/init-bashrc.sh" >> /root/.bashrc && \  
echo 'export PATH="/root/.composer/vendor/bin:$PATH"' >> /root/.bashrc  
  
#Start run shell  
CMD ["bash"]  
  

