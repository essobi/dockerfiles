FROM cloudhotspot/sample-django-app-base:latest  
MAINTAINER Justin Menga <justin.menga@cloudhotspot.co>  
  
# Install build dependencies  
RUN apt-get install -qy libffi-dev libssl-dev python-dev libmysqlclient-dev  
  
# Activate virtual environment and install wheel support  
RUN . /appenv/bin/activate && \  
pip install wheel  
  
# PIP environment variables (NOTE: must be set after installing wheel)  
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse
PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache  
  
# OUTPUT: Build artefacts (Wheels) are output here  
VOLUME /wheelhouse  
  
# INPUT: The application/project root to build from  
VOLUME /application  
WORKDIR /application  
  
# Add test entrypoint script  
ADD scripts/test.sh /usr/local/bin/test.sh  
RUN chmod +x /usr/local/bin/test.sh  
  
# Set defaults for entrypoint and command string  
ENTRYPOINT ["test.sh"]  
CMD ["python", "manage.py", "test"]

