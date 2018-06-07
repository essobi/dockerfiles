FROM python:3.6-slim  
MAINTAINER Greg Guthe <gguthe@mozilla.com>  
  
ENV PYTHONUNBUFFERED=1 \  
PYTHONPATH=/app/ \  
DJANGO_CONFIGURATION=Prod \  
PORT=8000  
# add a non-privileged user for installing and running the application  
# don't use --create-home option to prevent populating with skeleton files  
RUN mkdir /app && \  
chown 10001:10001 /app && \  
groupadd --gid 10001 app && \  
useradd --no-create-home --uid 10001 --gid 10001 --home-dir /app app  
  
# hack to make postgresql-client install work on slim  
RUN mkdir -p /usr/share/man/man1 \  
&& mkdir -p /usr/share/man/man7  
  
# install a few essentials and clean apt caches afterwards  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apt-transport-https build-essential curl git libpq-dev \  
postgresql-client iputils-ping ipmitool openssh-client \  
snmp && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Python dependencies  
COPY requirements.txt /tmp/  
COPY dev-requirements.txt /tmp/  
# Switch to /tmp to install dependencies outside home dir  
WORKDIR /tmp  
RUN pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt  
  
# Switch back to home directory  
WORKDIR /app  
  
COPY . /app  
  
RUN chown -R 10001:10001 /app  
  
USER 10001  
# Using /bin/bash as the entrypoint works around some volume mount issues on
Windows  
# where volume-mounted files do not have execute bits set.  
# https://github.com/docker/compose/issues/2301#issuecomment-154450785 has
additional background.  
ENTRYPOINT ["/bin/bash", "/app/bin/run.sh"]  
  
CMD ["web"]  

