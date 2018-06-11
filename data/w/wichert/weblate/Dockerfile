FROM ubuntu:16.04  
MAINTAINER Wichert Akkerman <wichert@wiggy.net>  
  
# Add user early to get a consistent userid  
RUN useradd --shell /bin/sh --user-group weblate  
  
RUN apt-get update  
RUN env DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends
-y ssh curl python-virtualenv python-lxml python-pillow python-psycopg2 git
python-dev build-essential nginx  
  
WORKDIR /app  
RUN python -m virtualenv --system-site-packages .  
ADD requirements.txt /tmp/requirements.txt  
RUN bin/pip install -r /tmp/requirements.txt  
RUN rm /tmp/requirements.txt  
  
WORKDIR /tmp  
  
RUN install -d -o root -g root -m 755 /app/etc  
RUN install -d -o weblate -g weblate -m 755 /app/data  
RUN install -d -o weblate -g weblate -m 755 /app/data/home  
RUN ln -s /app/data/home /home/weblate  
RUN cp /app/lib/python2.7/site-packages/weblate/settings_example.py
/app/etc/settings.py  
RUN ln -s /app/etc/settings.py /app/lib/python2.7/site-
packages/weblate/settings.py  
  
VOLUME ["/app/etc", "/app/data"]  
  
ENV DJANGO_SETTINGS_MODULE weblate.settings  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY runner /usr/local/bin/weblate-runner  
  
EXPOSE 8000  
ENTRYPOINT ["/usr/local/bin/weblate-runner"]  
CMD ["start"]  

