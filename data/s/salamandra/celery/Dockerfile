FROM salamandra/rsyslog  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python python-dev
python-pip  
RUN rm -rf /var/lib/apt/lists/*  
  
# install uWSGI  
RUN pip install "celery>=3.1,<3.2"  
  
# Create celery group  
RUN addgroup celery  
  
# Create celery user  
RUN adduser --disabled-password --home /data/app --no-create-home --system -q
--ingroup celery celery  
  
RUN mkdir /var/log/app/ -p  
RUN chown -R celery:celery /var/log/app/  
  
ADD supervisor/conf.d/ /etc/supervisor/conf.d/  
ADD run.sh /usr/local/bin/run.sh  
  
VOLUME ["/data/app/"]  
  
CMD ["/bin/sh", "-e", "/usr/local/bin/run.sh"]

