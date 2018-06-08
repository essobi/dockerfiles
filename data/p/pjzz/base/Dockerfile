# A good starting point  
FROM debian:7.3  
  
# make sure the package repository is up to date and update ubuntu  
RUN apt-get update # 20140326  
RUN apt-get -y upgrade  
  
# configure US locale  
RUN apt-get install -y locales  
RUN echo "en_US.UTF-8 UTF-8" >/etc/locale.gen  
RUN /usr/sbin/locale-gen  
RUN update-locale LANG=en_US.UTF-8  
  
# Add some extra utils that we often need  
RUN apt-get install -y wget  
  
# install supervisor to manage our processes  
# the supervisor config file is more likely to change and is therefore added
as a later step  
RUN apt-get -y install python-setuptools  
RUN easy_install supervisor  
RUN mkdir -p /var/log/supervisor  
# create directory for child images to store configuration in  
RUN mkdir -p /etc/supervisor/conf.d  
  
ADD supervisor.conf /etc/supervisor.conf  
  
# slim down some if possible  
RUN apt-get clean  

