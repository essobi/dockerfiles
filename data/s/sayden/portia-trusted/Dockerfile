# Select Fedora as base image  
FROM fedora  
  
MAINTAINER Mario Castro mariocaster@gmail.com  
  
# Install required dependencies and GIT to clone portia project  
RUN yum install -y --nogpgcheck gcc  
RUN yum install -y --nogpgcheck python  
RUN yum install -y --nogpgcheck git  
RUN yum install -y --nogpgcheck python-pip  
RUN yum install -y --nogpgcheck python-devel  
RUN yum install -y --nogpgcheck twisted python-twisted-runner  
RUN yum install -y --nogpgcheck python-lxml  
  
# Install required Portia package  
RUN pip install virtualenv  
RUN pip install loginform  
RUN pip install jsonschema  
RUN pip install scrapy  
RUN pip install -e git://github.com/scrapy/scrapely.git\#egg=scrapely  
  
# Clone portia project from github  
RUN git clone https://github.com/scrapinghub/portia.git /opt/portia  
  
# "Compile"? slybot  
RUN pip install -e /opt/portia/slybot  
  
# Expose the port used by portia  
EXPOSE 9001 22  
# Add the startup script  
ADD start-portia.sh /opt/portia/start-portia.sh  
  
# Start the web server  
CMD ["/opt/portia/start-portia.sh"]  

