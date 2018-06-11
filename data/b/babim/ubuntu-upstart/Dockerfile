FROM ubuntu-upstart  
  
MAINTAINER "Duc Anh Babim" <ducanh.babim@yahoo.com>  
  
RUN rm -f /etc/motd && \  
echo "---" > /etc/motd && \  
echo "Support by Duc Anh Babim. Contact: ducanh.babim@yahoo.com" >> /etc/motd
&& \  
echo "---" >> /etc/motd && \  
touch "/(C) Babim"  
  
## Enable Ubuntu Universe and Multiverse.  
RUN sed -i 's/^#\s*\\(deb.*universe\\)$/\1/g' /etc/apt/sources.list  
RUN sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list  
  
RUN apt-get clean && \  
apt-get update && \  
apt-get install locales wget nano -y  
  
## Fix locale.  
RUN dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 LANGUAGE=en_US:en
LC_ALL=en_US.UTF-8  
  
RUN apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove  
  
# Set environment variables.  
ENV HOME /root  
ENV LC_ALL en_US.UTF-8  
ENV TZ Asia/Ho_Chi_Minh  
# Define working directory.  
WORKDIR /root  

