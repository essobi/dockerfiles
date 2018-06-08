FROM ubuntu:16.04  
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>  
  
# Install packages from APT  
RUN \  
apt-get update && \  
apt-get install -y python-pip python-dev libpq-dev uwsgi uwsgi-plugin-python
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Install the PIP requirements  
COPY requirements.txt /root/  
RUN pip install -r /root/requirements.txt  
  
# Copy the source file and management script  
COPY numbles /root/numbles  
COPY manage.py /usr/local/bin  
  
# Set a couple of important environment variables  
ENV PYTHONPATH=/root \  
SITE_DOMAIN=numbles  
  
# Run the application through uWSGI  
CMD [ \  
"uwsgi", \  
"--http-socket", "0.0.0.0:80", \  
"--plugin", "python", \  
"--chdir", "/root", \  
"--module", "numbles.wsgi", \  
"--static-map", "/static=/data/static", \  
"--static-map", "/media=/data/media" \  
]  
  
# Expose port 80  
EXPOSE 80  

