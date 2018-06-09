FROM ubuntu:14.04  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc)
main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list && \  
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
sudo apt-get -y update && \  
sudo apt-get -y install nginx && \  
# Make www-data user uid/gid 1000 since this is the uid that boot2docker  
# will use for mounted directories.  
usermod -u 1000 www-data && \  
groupmod -g 1000 www-data  
  
ADD entrypoint.sh /entrypoint.sh  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD default /etc/nginx/sites-available/default  
  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
EXPOSE 80

