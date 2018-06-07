# Base system is the LTS version of Ubuntu.  
FROM ubuntu:14.04  
# Make sure we don't get notifications we can't answer during building.  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV VIRTUAL_HOST localhost  
ENV VIRTUAL_PORT 80  
# Default User  
ENV USER user  
ENV PASS pass  
  
# Process User ID  
ENV UID 1000  
# Download and install everything from the repos.  
# Java  
RUN apt-get --yes update; apt-get --yes upgrade; apt-get --yes install
software-properties-common  
RUN sudo apt-add-repository --yes ppa:webupd8team/java; apt-get --yes update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get --yes install curl oracle-java8-installer unzip git curl  
  
RUN apt-get --yes install apache2 php5 php5-curl libapache2-mod-php5 mysql-
server mysql-client php5-mysql  
  
# Config for Apache  
ADD apache2/http.conf /etc/apache2/http.conf  
ADD apache2/000-default /etc/apache2/sites-available/000-default.conf  
  
# Download SpaceBukkit  
RUN rm -rf /var/www && \  
git clone https://github.com/XereoNet/SpaceBukkitPanel /var/www && \  
mkdir /data && \  
chown -R www-data:www-data /var/www && \  
chown -R www-data:www-data /data && \  
a2enmod rewrite && \  
service apache2 restart  
  
# Add remote toolkit temporary directory  
ADD ./mcrtoolkit/ /mcrtoolkit/  
  
# Load in all script files.  
ADD ./scripts/start /start  
  
# Fix all permissions  
RUN chmod +x /start  
  
# 80 for Webserver  
EXPOSE 80  
# 25565 is for minecraft  
EXPOSE 25565  
# 25561 is for telnet  
EXPOSE 25561  
# /data contains the Minecraft data  
VOLUME ["/data"]  
  
# /start runs it.  
CMD ["/start"]

