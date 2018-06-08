FROM ubuntu:14.04  
MAINTAINER Stas Solodkin <stas@oscar3cp.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG hostname=portal  
ARG password=I2grep4u  
  
RUN touch /etc/init.d/systemd-logind  
  
RUN apt-get update && apt-get install -y \  
openssh-server \  
git \  
tar \  
zip \  
net-tools \  
dnsutils \  
sysstat \  
dnsutils \  
curl \  
libcurl3 \  
libcurl3-dev \  
fop \  
software-properties-common \  
python-software-properties  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:$password' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN echo "export EDITOR=vi" >> /etc/profile  
  
RUN apt-get update && apt-get -f install  
  
RUN apt-get install -y apache2  
RUN echo "ServerName $hostname" >> /etc/apache2/apache2.conf  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN echo mysql-server mysql-server/root_password password $password | debconf-
set-selections;\  
echo mysql-server mysql-server/root_password_again password $password |
debconf-set-selections;\  
apt-get install -y mysql-server libapache2-mod-auth-mysql  
  
RUN cp /etc/mysql/my.cnf /usr/share/mysql/my-default.cnf  
RUN mysql_install_db  
#RUN mysql_install_db --explicit_defaults_for_timestamp  
#RUN usermod -d /var/lib/mysql/ mysql  
ADD my.cnf /etc/mysql/my.cnf  
RUN chmod 644 /etc/mysql/my.cnf  
#  
RUN service mysql start && \  
mysql -u root -p"$password" -e "DELETE FROM mysql.user WHERE User='root' AND
Host NOT IN ('localhost', '127.0.0.1', '::1')" && \  
mysql -u root -p"$password" -e "DELETE FROM mysql.user WHERE User=''" && \  
mysql -u root -p"$password" -e "DELETE FROM mysql.db WHERE Db='test' OR
Db='test\\_%'" && \  
mysql -u root -p"$password" -e "FLUSH PRIVILEGES"  
  
ENV LANG C.UTF-8  
RUN sudo add-apt-repository ppa:ondrej/php  
RUN sudo apt-get -y update  
RUN sudo apt-get -y install php5.6 php5.6-mcrypt php5.6-mbstring php5.6-curl
php5.6-mysql php5.6-cli php5.6-gd php5.6-intl php5.6-xsl  
  
ADD php.ini /etc/php/5.6/apache2/php.ini  
RUN chmod 644 /etc/php/5.6/apache2/php.ini  
  
ADD dir.conf /etc/apache2/mods-enabled/dir.conf  
  
RUN a2enmod rewrite  
RUN a2enmod ssl  

