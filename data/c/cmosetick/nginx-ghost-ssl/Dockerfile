# Pull base image.  
FROM ubuntu:14.04  
# Do APT work first  
RUN \  
#Use preferred Ubuntu mirror  
sed -i 's@http://archive.ubuntu.com/ubuntu/@http://ubuntu.osuosl.org/ubuntu@g'
/etc/apt/sources.list && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
# apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl wget git htop unzip man && \  
add-apt-repository -y ppa:nginx/stable  
  
# Install Nginx stable version from PPA  
RUN \  
apt-get update && \  
apt-get install -y nginx-full && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certificates",
"/var/log/nginx"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Add files.  
ADD files/start.bash /usr/local/bin/  
  
# Define default command.  
CMD ["bash", "start.bash"]  
  
# Expose ports.  
EXPOSE 80 443  

