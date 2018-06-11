FROM python:2.7  
MAINTAINER The Netyeti <netyeti@thenetyeti.com>  
  
  
# Set the target directory that we will be working in  
WORKDIR /usr/src/djangoproject  
  
# Add in the initialization script and run it  
COPY ./initialize /usr/local/bin/  
COPY ./defaults.ini /etc/djangocms/defaults.ini  
RUN chmod +x /usr/local/bin/initialize  
  
# Upgrade pipand install DjangoCMS  
RUN pip install --no-cache-dir --upgrade pip  
RUN pip install --no-cache-dir djangocms-installer  
  
# Change the ownership to the default user  
RUN groupadd -g 1000 gjangouser && \  
useradd -r -u 1000 -g 1000 djangouser && \  
chown -R djangouser /usr/src/djangoproject  
####TODO: variablize the user and group so that it can be set from a compose
file or command line  
####TODO: add settings file changes/checks for MySQL usage  
# Create a useful volume to attatch to  
VOLUME /usr/src/djangoproject  
  
EXPOSE 8000  
# Start it up!  
CMD [ "python" ]  
  
###  
#  
# USAGE EXAMPLE:  
#  
# docker run --rm -v $PWD/djangoproject:/usr/src/djangoproject -it
yeticraft/djangocms_base initialize  
#  
# This will run the DjangoCMS wizard and generate the project files on the
host system. Next step is to create your  
# own Dockerfile, docker-compose.yml and project around it.  
#  
###

