FROM damienlagae/lamp  
MAINTAINER Damien Lagae <damien@lagae.info>  
  
# Install required packages & cleanup  
RUN apt-get clean all && \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install openssl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Adding the Configuration File for host  
ADD conf/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD shell/run.sh /run.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/apache2/access-ssl.log && \  
ln -sf /dev/stderr /var/log/apache2/error-ssl.log  
  
# Give the execution permissions  
RUN chmod 755 /*.sh  
  
# Enable apache mods  
RUN a2enmod ssl  
  
# Create SSL certificate  
RUN mkdir -p /etc/apache2/ssl/ && \  
openssl req -x509 -nodes -sha256 -days 3650 -subj
"/C=BE/ST=Brussels/CN=localhost" -newkey rsa:2048 -keyout
"/etc/apache2/ssl/key.pem" -out "/etc/apache2/ssl/cert.pem"  
  
# Set the port  
EXPOSE 1080 80 443 3306 9000  
# Set working directory  
WORKDIR /var/www/html  
  
# Execut the run.sh  
CMD ["/run.sh"]  

