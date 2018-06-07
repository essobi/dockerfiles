# Set the base image to use to Ubuntu  
FROM himnark/ocr-engine:develop  
  
# Set the file maintainer  
MAINTAINER Armine Hayrapetyan <armine_h@instigatedesign.com>  
  
# Update the default application repository sources list  
RUN apt-get update && apt-get -y upgrade  
  
# Make idoodi directory  
RUN cd /srv/himnark && mkdir idoodi  
  
# Get IDOODI repo  
COPY / /srv/himnark/idoodi  
  
# Copy entrypoint script into the image  
COPY ./install.sh /  
RUN /bin/bash /install.sh  
  
# Install mysql backend connector  
RUN apt-get install -y python-mysqldb  
  
# runserver  
ENTRYPOINT cd /srv/himnark/idoodi/src/server && python manage.py migrate
--noinput && python manage.py loaddata predefined_data.json && python
manage.py runserver 0.0.0.0:80 && /bin/bash  

