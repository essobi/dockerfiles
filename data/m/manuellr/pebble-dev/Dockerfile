FROM ubuntu:16.04  
MAINTAINER ManuelLR  
  
# update system and get base packages  
RUN apt-get update && \  
apt-get install -y curl nodejs npm python2.7-dev python-pip libfreetype6-dev
bash-completion libsdl1.2debian libfdt1 libpixman-1-0 libglib2.0-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set the version of the pebble tool  
ENV PEBBLE_TOOL_VERSION pebble-sdk-4.5-linux64  
  
# set the symbolic link for nodejs to node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# get pebble tool  
RUN curl -SL https://s3.amazonaws.com/assets.getpebble.com/pebble-
tool/${PEBBLE_TOOL_VERSION}.tar.bz2 \  
| tar -C /opt/ --totals -xj && echo "PEBBLE_TOOL downloaded !"  
  
# prepare python environment  
WORKDIR /opt/${PEBBLE_TOOL_VERSION}  
RUN /bin/bash -c " \  
pip install virtualenv && \  
virtualenv --no-site-packages .env && \  
source .env/bin/activate && \  
pip install -r requirements.txt && \  
deactivate " && \  
rm -r /root/.cache/  
  
# prepare pebble user for build environment + enable analytics  
RUN adduser --disabled-password --gecos "" \--ingroup users pebble && \  
echo "pebble ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
chmod -R 777 /opt/${PEBBLE_TOOL_VERSION} && \  
mkdir -p /home/pebble/.pebble-sdk/ && \  
chown -R pebble:users /home/pebble/.pebble-sdk && \  
touch /home/pebble/.pebble-sdk/ENABLE_ANALYTICS  
  
# change to pebble user  
USER pebble  
  
# set PATH  
ENV PATH
/opt/${PEBBLE_TOOL_VERSION}/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# prepare project mount path  
VOLUME /pebble/  
  
# set run command  
WORKDIR /pebble/  
  
# set the version of the pebble sdk  
ENV PEBBLE_SDK_VERSION 4.3  
# install sdk  
RUN /bin/bash -c 'yes | pebble sdk install ${PEBBLE_SDK_VERSION}'  
  
CMD /bin/bash  
  

