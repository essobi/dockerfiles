FROM ubuntu:xenial  
# another thing  
# another commrnt to trigger a build  
# other default things  
# default stuff  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
manpages \  
man-db \  
git \  
ssh \  
vim \  
tree \  
nmap \  
htop \  
python-dev  
  
# Install pip with pip (inceptionise!)  
# Remove the old pip afterwards to avoid confusion  
# pin to 8.1.1 because 8.1.2 has some incompatibilities with salt  
RUN set -ex; \  
apt-get install -y python-pip; \  
pip install -I pip==8.1.1; \  
apt-get purge -y python-pip  
  
RUN mkdir -p /root/.ssh  
  

