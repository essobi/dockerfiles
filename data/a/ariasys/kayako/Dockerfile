FROM marvambass/nginx-ssl-php  
MAINTAINER AriaSys Technology <ariasystech@gmail.com>  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
  
RUN echo "mysql-server mysql-server/root_password password rootpass" |
debconf-set-selections  
RUN echo "mysql-server mysql-server/root_password_again password rootpass" |
debconf-set-selections  
  
ADD install.sh /opt/install.sh  
RUN chmod a+x /opt/install.sh  
COPY kayako.tar.gz /opt/kayako.tar.gz  
  
RUN apt-get update && apt-get install -y mysql-server \  
vim wget net-tools php5 php5-cli php5-mysql \  
php5-mcrypt php5-gd php5-curl php5-imap && \  
php5enmod mcrypt && \  
php5enmod imap  
  
RUN sed -i 's/# exec CMD/\/opt\/install.sh\n# exec CMD/g' /opt/entrypoint.sh  

