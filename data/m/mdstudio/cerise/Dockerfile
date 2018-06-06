FROM ubuntu:16.04  
MAINTAINER Lourens Veen <l.veen@esciencecenter.nl>  
  
# Install requirements  
RUN apt-get update -y && apt-get -y dist-upgrade && \  
apt-get install -y --no-install-recommends python3 python3-pip \  
python3-setuptools python3-wheel python3-dev build-essential \  
default-jre nginx-full less python python-pip python-setuptools \  
python-wheel python-all-dev && \  
pip install cwltool cwlref-runner && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add service user  
RUN useradd cerise && mkdir /home/cerise && chown cerise:cerise /home/cerise  
  
# Set up WebDAV directories and give service access  
RUN mkdir -p /home/webdav/files/input && mkdir /home/webdav/client_temp && \  
chown -R www-data:www-data /home/webdav && \  
chmod 775 /home/webdav /home/webdav/files /home/webdav/files/input && \  
usermod -a -G www-data cerise  
  
# Set up service run dirs  
# We make these in advance to avoid race conditions between the gunicorn  
# worker processes; these may otherwise crash trying to make the same  
# directory simultaneously  
RUN mkdir /home/cerise/run && \  
mkdir /home/cerise/run/jobs && \  
mkdir /home/cerise/run/files && \  
chown -R cerise:cerise /home/cerise/run && \  
mkdir /home/cerise/conf && \  
chown cerise:cerise /home/cerise/conf && \  
mkdir /var/log/cerise && mkdir /var/log/gunicorn && \  
chown cerise:root /var/log/cerise /var/log/gunicorn  
  
# Make service dir and install dependencies  
COPY requirements.txt /home/cerise  
WORKDIR /home/cerise  
RUN pip3 install -r requirements.txt  
  
# Copy software into container  
COPY cerise /home/cerise/cerise  
COPY api /home/cerise/api  
COPY conf/docker-config.yml /home/cerise/conf/config.yml  
RUN chown -R cerise:cerise /home/cerise && \  
rm -f /home/cerise/run/cerise.db  
  
# Copy WebDAV configuration  
COPY conf/docker-nginx.conf /etc/nginx/sites-available/default  
  
# Copy init script  
COPY conf/docker-init.sh /usr/local/bin/init.sh  
RUN chmod 755 /usr/local/bin/init.sh  
  
# Start the service  
CMD ["/bin/bash", "/usr/local/bin/init.sh"]  
  

