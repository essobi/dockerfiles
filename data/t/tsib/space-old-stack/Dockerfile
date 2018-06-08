FROM ubuntu:precise  
  
# Install base packages  
RUN apt-get -y update  
RUN apt-get -y install python-software-properties  
RUN apt-get update && apt-get -yq install apache2  
RUN apt-get -y install curl  
RUN apt-get -y install libapache2-mod-php5  
RUN add-apt-repository ppa:ondrej/php5  
RUN apt-get -y update  
RUN apt-get -y install php5  
RUN apt-get -y install php5-mysql  
RUN apt-get -y install php5-mcrypt  
RUN apt-get -y install php5-gd  
RUN apt-get -y install php5-curl  
RUN apt-get -y install php-pear  
RUN apt-get -y install php-apc  
RUN rm -rf /var/lib/apt/lists/* && curl -sS https://getcomposer.org/installer
| php -- --install-dir=/usr/local/bin --filename=composer  
RUN apt-get -y install php5-mysql  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **False**  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure /app folder with sample app  
RUN mkdir -p /var/www/html  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/run.sh"]  

