FROM python:3-slim  
  
# Expect to find the entrypoint script at /entrypoint  
ENTRYPOINT ["/entrypoint"]  
  
# Debug tools  
RUN pip3 install ipdb  
  
# Supporting libraries for python modules  
RUN apt-get update && apt-get install --yes libpq-dev build-essential  
  
# Default config for where we expect to find requirements  
ENV REQUIREMENTS_PATH="requirements.txt"  
ENV REQUIREMENTS_HASH="/usr/local/lib/python3.6/site-
packages/requirements.md5"  
# Ensure all users can create dependencies  
RUN chmod -R 777 /usr/local/lib/python3.6/site-packages/ /usr/local/bin/
/usr/local/share/  
  
# Create a shared home directory  
# This helps anonymous users have a home  
ENV HOME=/home/shared  
RUN mkdir -p $HOME  
RUN chmod -R 777 $HOME  
  
# Add binaries to image  
ADD entrypoint /entrypoint  
  

