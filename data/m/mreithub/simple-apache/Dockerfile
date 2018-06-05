FROM debian:stretch  
  
MAINTAINER manuel@reithuber.net  
  
# Install packages  
RUN apt-get update && apt-get -y install apache2 python3-pip git libssl-dev
libffi-dev cron  
  
# Install simp-le (letsencrypt.org client)  
RUN pip3 install git+https://github.com/zenhack/simp_le.git  
  
# install required pypi packages  
RUN pip3 install --upgrade six setuptools cryptography  
  
RUN a2enmod proxy_http rewrite ssl  
  
# Create simp_le user (and add it to the ssl-cert group)  
RUN adduser --disabled-password --no-create-home --gecos "simp_le user" simp-
le  
RUN adduser simp-le ssl-cert  
  
# test things (the mix of apt-get and pip python modules sometimes messes
things up)  
RUN simp_le --help > /dev/null  
  
VOLUME /etc/apache2/ssl/  
VOLUME /etc/apache2/sites-available/  
VOLUME /var/www/  
  
COPY res/ /  
  
# create some working dirs (without them apache refuses to run)  
RUN mkdir -p /var/lock/apache2/ /var/run/apache2/  
RUN chown www-data /var/lock/apache2/  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT [ "/run.sh" ]  
  

