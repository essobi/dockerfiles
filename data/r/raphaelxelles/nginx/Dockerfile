from ubuntu:precise  
  
maintainer Raphael  
  
run apt-get update  
# Install Nginx  
run apt-get update  
run apt-get install -y build-essential  
run apt-get install -y python python-dev python-setuptools  
run apt-get install -y nginx supervisor curl  
  
# install nginx  
run apt-get install -y python-software-properties  
run apt-get update  
RUN add-apt-repository -y ppa:nginx/stable  
  
# Install confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.3.0/confd_0.3.0_linux_amd64.tar.gz
| tar xz  
RUN mv confd /usr/local/bin/confd  
  
# Create directories  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
  
# Add confd files  
ADD ./confd /etc/confd/  
  
# Remove default site  
RUN rm -f /etc/nginx/sites-enabled/default  
  
# Add boot script  
ADD ./bin/boot.sh /boot.sh  
RUN chmod +x /boot.sh  
  
# Run the boot script  
CMD /boot.sh  

