# Pull in the from the official python image.  
FROM python:3  
  
# Optionally set a maintainer name to let people know who made this image.  
MAINTAINER Nicolai Hald <haldcph@gmail.com>  
  
  
###############################################################################  
# INSTALLATION  
###############################################################################  
  
RUN set -x \  
&& mkdir -p /app/logs \  
&& mkdir -p /app/data  
# && apt-get update \  
# && apt-get clean \  
# && rm -rf /var/lib/apt/lists/*  
  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
# Create a system group and user to be used by HAProxy.  
RUN groupadd exporter && useradd -g exporter exporter  
  
# ### tweak image set-up  
RUN pip install pyyaml elasticsearch boto3 psutil  
  
###############################################################################  
# DATA  
###############################################################################  
VOLUME ["/app", "/app_logs","/app_data"]  
WORKDIR /app  
  
COPY root/ /  
  
RUN chmod +x /docker-entrypoint.sh \  
# Set logstash as the owner of the /data directory - otherwise we'll get a
permission denied exception  
&& chown -hR exporter:exporter /app \  
&& chmod -R 777 /app  
  
# install the actual app  
RUN python ./setup.py install --force  
  
###############################################################################  
# START  
###############################################################################  
  
# Allow us to customize the entrypoint of the image.  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
  
# Start python in the foreground to play nicely with Docker.  
# CMD [ "python", "/app/test.py" ]  
# CMD [ "python", "/app/exporter.py" ]  
CMD [ "searchlog_exporter" ]  
  
EXPOSE 9200 9300 21 50000-50100

