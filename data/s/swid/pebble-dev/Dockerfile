FROM ubuntu:12.04  
MAINTAINER Sumedha Widyadharma <sumedha@widyadharma.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV force_color_prompt yes  
  
ENV SDK_NAME PebbleSDK-2.8.1  
# Package setup  
RUN apt-get update && \  
apt-get install -y wget \  
curl \  
git \  
vim \  
sudo \  
python-pip \  
python2.7-dev \  
python-virtualenv && \  
apt-get purge -y nano && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set up user  
RUN adduser --disabled-password --gecos "" pebble && \  
echo "pebble ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
echo "/usr/local/bin/fetch-sdk.sh" >> /home/pebble/.bashrc && \  
echo "export PATH=~/pebble-dev/$SDK_NAME/bin:$PATH" >> /home/pebble/.bashrc &&
\  
echo "test -e ~/.sdk_ready || echo -e '\n\tError: The SDK is not ready, run
fetch-sdk.sh\n'" >> /home/pebble/.bashrc && \  
echo "echo -e '\n\tDo not forget to set your PEBBLE_PHONE\n'" >>
/home/pebble/.bashrc  
  
# If you have these files and want to rebuild the image, this will speed up
the first run significantly  
#COPY PebbleSDK-2.8.1.tar.gz /home/pebble/  
#COPY arm-cs-tools-stripped.tar /home/pebble/  
COPY fetch-sdk.sh /usr/local/bin/  
  
USER pebble  
WORKDIR /home/pebble  
CMD /bin/bash -i  

