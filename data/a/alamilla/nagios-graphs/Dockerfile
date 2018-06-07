# nagios-graphs  
#  
# VERSION 1.0  
FROM alamilla/nagios  
MAINTAINER Andres F. Lamilla, "aflamillac@gmail.com"  
# https://www.solucions-im.com/blogs/tecnic/pnp4nagios-0-6-24-en-5-minutos-en-
nagios-4-0-8/  
# Install dependencies  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
\  
rrdtool \  
librrds-perl  
  
# Download and install pnp4nagios  
RUN wget -O pnp4nagios.tar.gz
https://sourceforge.net/projects/pnp4nagios/files/latest/download && \  
tar xzvf pnp4nagios.tar.gz && \  
cd pnp4nagios-0.6.25 && \  
./configure && \  
make all && \  
make fullinstall && \  
cp contrib/ssi/status-header.ssi /usr/local/nagios/share/ssi/  
  
RUN rm -rf /usr/local/pnp4nagios/share/install.php  
  
# Enable site pnp4nagios in apache2  
RUN cp /etc/httpd/conf.d/pnp4nagios.conf /etc/apache2/sites-available/ && \  
a2ensite pnp4nagios  
  
# Copy npcd service init script in /etc/service  
COPY ./etc /etc  
  
# Copy nagios templates with pnp  
COPY ./nagios /usr/local/nagios/etc  
  
EXPOSE 80  

