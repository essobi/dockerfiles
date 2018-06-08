FROM ubuntu:saucy  
MAINTAINER roli keusch <mail@keus.ch>  
  
# Update Ubuntu to the latest  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
# Install needed Softwares  
RUN apt-get install -y wget curl python-dev build-essential git python-pip
python-setuptools  
  
# Grab the latest Mist.io Version and install it  
RUN git clone https://github.com/mistio/mist.io.git /opt/mistio  
RUN cd /opt/mistio  
WORKDIR /opt/mistio  
RUN /usr/bin/pip install setuptools --upgrade  
RUN /usr/bin/python bootstrap.py  
RUN /opt/mistio/bin/buildout -v  
  
# Clean up  
RUN apt-get autoremove && apt-get autoclean  
  
# Expose port  
EXPOSE 6543  
# Additional Files  
ADD ./mistio-run.sh /mistio-run.sh  
RUN chmod 755 /mistio-run.sh  
ADD ./settings.py /opt/mistio/  
  
# Start Mist.io  
CMD ["/bin/bash", "/mistio-run.sh"]  

