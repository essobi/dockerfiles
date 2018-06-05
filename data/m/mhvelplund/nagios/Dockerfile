# Nagios server with web config UI  
FROM ubuntu:14.04.2  
MAINTAINER Mads Hvelplund "mhv@tmnet.dk"  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq  
RUN apt-get install -y apache2 libapache2-mod-php5 build-essential libgd-dev
wget apache2-utils  
  
# Create the nagios user and groups  
RUN useradd -m nagios  
RUN groupadd nagcmd  
RUN usermod -a -G nagcmd nagios  
RUN usermod -a -G nagcmd www-data  
  
# Download the software  
RUN mkdir download  
WORKDIR download  
RUN wget
http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-3.5.1.tar.gz  
RUN wget http://nagios-plugins.org/download/nagios-plugins-2.0.3.tar.gz  
RUN tar xvzf nagios-3.5.1.tar.gz  
RUN tar xvzf nagios-plugins-2.0.3.tar.gz  
  
# Compile Nagios  
WORKDIR /download/nagios  
RUN ./configure --with-command-group=nagcmd  
RUN make all  
RUN make install  
RUN make install-init  
RUN make install-config  
RUN make install-commandmode  
# make install-webconf is broken; do it manually  
RUN install -c -m 644 sample-config/httpd.conf /etc/apache2/conf-
available/nagios.conf  
RUN a2enconf nagios  
RUN a2enmod cgi  
  
# Compile Nagios Plugins  
WORKDIR /download/nagios-plugins-2.0.3/  
RUN ./configure --with-nagios-user=nagios --with-nagios-group=nagios  
RUN make  
RUN make install  
WORKDIR /  
  
# Add mail support  
RUN apt-get -y install bsd-mailx postfix  
  
# Cleanup  
RUN rm -rf /download  
RUN apt-get -y remove build-essential  
RUN apt-get -y autoclean  
RUN apt-get -y clean  
RUN apt-get -y autoremove  
  
#Add startup script  
ADD entrypoint.sh /entrypoint.sh  
  
# Expose ports  
EXPOSE 80  
# Start Nagios and Apache2  
CMD ["/entrypoint.sh"]  
  

