# Use Rafael's base Django image available at
https://hub.docker.com/r/rafaelpivato/django/  
FROM rafaelpivato/django  
  
# Copy requirements.txt into the working directory of the container  
COPY requirements.txt ./  
  
# Install all requirements in the container's root Python installation  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy the rest of the application code into the working directory of the
container  
COPY . ./  
  
# Set the DJANGO_SETTINGS_MODULE env var to dojos.docker_settings  
ENV DJANGO_SETTINGS_MODULE=dojos.docker_settings  
  
# Collect static assets - since we're using dojos.docker_settings, this will
put the  
# static files in the container's /srv/static directory.  
RUN python manage.py collectstatic --no-input  

