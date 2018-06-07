# This builds a basic docker image that runs the latest  
# version of happening  
# It expects a Postgres server, and a Redis server  
# to be running externally  
# Set the DATABASE_URL environment variable to point to the postgres server  
# If you want to store uploaded media on the filesystem you must bind to  
# the /happening/src/media directory  
# To use AWS you must set the environment variables AWS_ACCESS_KEY_ID  
# AWS_SECRET_ACCESS_KEY and S3_BUCKET_NAME  
# To use emails - add SENDGRID_USERNAME and SENDGRID_PASSWORD environment
variables  
# To use Sentry for logging add SENTRY_DSN environemnt variable  
# DJANGO_DEBUG can be set to enable debug mode  
FROM python:3.4  
MAINTAINER "jonathan@jscott.me"  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install -y git-all nodejs  
  
# TODO: Restore this once we have stable tagging --branch latest  
# This ensures that the latest version of the git code will be pulled -
avoiding cache  
ADD https://api.github.com/repos/happeninghq/happening/git/refs/heads/master
version.json  
RUN git clone https://github.com/happeninghq/happening.git happening  
  
RUN pip3 install --upgrade pip  
RUN pip3 install -r happening/src/requirements.txt  
RUN cd happening/src && npm install && npm install -g webpack && webpack  
RUN cd happening/src && python manage.py collectstatic --noinput  
  
WORKDIR /happening/src  
ENTRYPOINT ["python", "docker_web_entry.py"]  
  
EXPOSE 8000  

