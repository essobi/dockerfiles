FROM ubuntu:14.04  
ENV REFRESHED_AT 2015-08-28  
RUN apt-get -qq update  
  
# Install php and python  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y install php5 php5-cli php5-cgi php5-curl php5-gd php5-imagick
php5-mysqlnd php5-memcached \  
php5-intl php5-mcrypt php5-xdebug \  
python python-dev python-pip  
  
# Add users  
RUN adduser devel --home /home/devel \  
\--shell /bin/bash \  
\--disabled-password \  
\--gecos ""  
  
# Add users to sudoers, so no need to ask for password  
RUN echo "devel ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Make ports accessible  
EXPOSE 8080  
EXPOSE 8000  
# Install dependencies  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y install git curl make fabric nano unzip && \  
pip install Fabric==1.10.0 sphinx==1.2.3  
  
# Install App Engine SDK  
ADD https://storage.googleapis.com/appengine-
sdks/featured/google_appengine_1.9.25.zip /tmp/gae.zip  
RUN cd /usr/share && unzip /tmp/gae.zip  
  
# Configuration  
RUN rm /etc/php5/cgi/conf.d/20-memcached.ini && \  
echo "extension = mcrypt.so" > /etc/php5/cgi/conf.d/20-mcrypt.ini && \  
echo "extension = mcrypt.so" > /etc/php5/cli/conf.d/20-mcrypt.ini  
  
# Add application directory  
RUN mkdir -p /var/www/  
  
# Starting directory  
WORKDIR /var/www/  
  
# Starting user  
USER devel  
  
# Run the dev server  
CMD ["/usr/share/google_appengine/dev_appserver.py", "--
php_executable_path=/usr/bin/php-cgi", \  
"--host=0.0.0.0", "--admin_host=0.0.0.0", "--php_remote_debugging=yes", "--
skip_sdk_update_check=yes", "."]  

