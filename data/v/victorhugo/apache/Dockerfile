FROM victorhugo/debian:latest  
MAINTAINER VictorHugo <victorhugo.avila.cl@gmail.com>  
  
# Disable interactive functions  
#ENV DEBIAN_FRONTEND noninteractive  
# Updating the SO and Installing useful tools  
RUN apt-get update && apt-get install -y \  
apache2  
  
# Cleaning the apt/list repo  
RUN rm -rf /var/lib/apt/lists/*  
  
# Configuring Apache as a service  
RUN systemctl enable apache2.service  
RUN printf "export PATH=\"$PATH:/usr/sbin/\"" >> ~/.profile  
RUN export PATH="$PATH:/usr/sbin/"  
  
# Copying configuration files  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY security.conf /etc/apache2/conf-enabled/  
  
# Securing the config  
#RUN a2dissite default  
RUN rm -r /var/www/html/index.*  
#RUN a2dismod autoindex -f  
RUN apachectl restart  
  
# Setting permissions  
RUN chmod 555 /var/www/  
RUN chmod 777 /var/www/html  
  
# Preparing a test  
RUN touch /var/www/html/index.html  
RUN printf '%s\n' '<html><body><h1>I&#39m Running!</h1><br><h4>Test provided
by: victorhugo.avila@easy-point.com</h4></body></html>' >>
/var/www/html/index.html  
  
# Expose the 80 port and 443 port  
EXPOSE 22 80 443  

