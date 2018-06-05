# Use an official Python runtime as a parent image  
FROM fedora:26  
MAINTAINER "Wenhan Shi" <wenshi@redhat.com>  
  
RUN yum update -y; yum clean all  
  
# Install needed packages  
RUN yum -y install firefox \  
xorg-x11-server-Xvfb \  
xorg-x11-fonts-Type1 \  
xorg-x11-fonts-75dpi \  
cronie \  
httpd \  
wget \  
mod_wsgi \  
systemd  
  
# start services  
RUN systemctl enable httpd.service  
RUN systemctl enable crond.service  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Copy and untar webdriver for firefox  
ADD
https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
/app  
RUN tar xf /app/geckodriver-v0.18.0-linux64.tar.gz -C /usr/local/bin #
geckodriver  
RUN mkdir /etc/freshcase  
RUN mv ecs.db /etc/freshcase  
RUN cp www/* /var/www/html/  
  
# Install requirements for python  
RUN pip3 install -r requirements.txt  
  
# Make port 80 available to the world outside this container  
EXPOSE 80  
# Define environment variable  
ENV NAME ahFreshCase  
  
RUN cat crontab >> /etc/crontab  
  
# Run ./initConfig.py when the container launches  
# ENTRYPOINT ["./initConfig.py"]  
CMD ["/usr/sbin/init"]  

