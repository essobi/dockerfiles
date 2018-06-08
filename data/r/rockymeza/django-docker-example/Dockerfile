FROM google/python  
  
# Ideally I could extract these to another Dockerfile with the ONBUILD  
# instruction  
WORKDIR /app  
  
RUN virtualenv /env  
  
# [Optional] If you are building from within China, I recommend uncommenting  
# this line.  
# ADD chinese-sources.list /etc/apt/sources.list  
# Required for psycopg2  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update -y && \  
apt-get install -y libpq-dev  
  
RUN /env/bin/pip install uwsgi  
  
# This will invalidate the cache everytime the requirements.txt file is  
# changed, so we want don't want to impact anything with apt.  
ADD requirements.txt /app/requirements.txt  
  
RUN /env/bin/pip install -r requirements.txt  
  
CMD ["/env/bin/uwsgi", "uwsgi.ini"]  
ENTRYPOINT []  
  
ADD . /app  

