FROM ubuntu:xenial  
  
# deployment "config"  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH $PATH:/usr/local/bin  
ENV DEPLOY_SITE shihooghan-dev  
  
CMD ["/usr/bin/topc"]  
  
EXPOSE 5000  
# start grabbing ubuntu dependencies  
RUN apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get install -y \  
git \  
build-essential \  
python3-dev \  
python3-pip \  
binutils \  
libproj-dev \  
libgeos-c1v5 \  
gdal-bin \  
libpq-dev \  
postgresql-9.5-postgis-2.1 \  
libffi6 \  
libffi-dev  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# setup deployment keys  
ADD config/docker/production/.ssh/id_rsa /root/.ssh/id_rsa  
ADD config/docker/production/.ssh/id_rsa.pub /root/.ssh/id_rsa.pub  
  
RUN chmod 600 /root/.ssh/id_rsa && \  
chmod 644 /root/.ssh/id_rsa.pub && \  
chown -R root:root /root/.ssh  
  
ADD config/docker/production/setup.sh /usr/bin/topc_setup  
RUN /usr/bin/topc_setup  
  
ADD config/docker/production/topc.sh /usr/bin/topc  

