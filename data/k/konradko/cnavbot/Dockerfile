# base resin image for python  
FROM resin/raspberrypi3-python  
  
ENV HOME=/root  
  
# Install papertrail config  
COPY config/papertrail/papertrail.service /etc/systemd/system/  
  
# Install required packages and remove the apt list to reduce the size of the
image  
RUN apt-get clean && apt-get update && apt-get install -yq --no-install-
recommends \  
openssh-server \  
nmap \  
bluetooth \  
bluez \  
bluez-firmware \  
libbluetooth-dev \  
libudev-dev \  
libopencv-dev \  
python-opencv \  
build-essential \  
libc6-dev \  
libboost-all-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Prometheus  
ENV PROMETHEUS_VERSION 0.20.0  
ENV NODE_EXPORTER_VERSION 0.12.0  
ENV ALERTMANAGER_VERSION 0.2.0  
ENV DIST_ARCH linux-armv7  
  
# default configs  
ENV THRESHOLD_CPU 50  
ENV THRESHOLD_FS 50  
ENV THRESHOLD_MEM 500  
ENV STORAGE_LOCAL_RETENTION 360h0m0s  
  
# Set prometheus working directory  
WORKDIR /etc  
  
# prometheus server  
RUN wget
https://github.com/prometheus/prometheus/releases/download/$PROMETHEUS_VERSION/prometheus-$PROMETHEUS_VERSION.$DIST_ARCH.tar.gz
\  
&& tar xvfz prometheus-$PROMETHEUS_VERSION.$DIST_ARCH.tar.gz \  
&& rm prometheus-$PROMETHEUS_VERSION.$DIST_ARCH.tar.gz  
  
# prometheus alertmanager  
RUN wget
https://github.com/prometheus/alertmanager/releases/download/$ALERTMANAGER_VERSION/alertmanager-$ALERTMANAGER_VERSION.$DIST_ARCH.tar.gz
\  
&& tar xvfz alertmanager-$ALERTMANAGER_VERSION.$DIST_ARCH.tar.gz \  
&& rm alertmanager-$ALERTMANAGER_VERSION.$DIST_ARCH.tar.gz  
  
# node exporter  
RUN wget
https://github.com/prometheus/node_exporter/releases/download/$NODE_EXPORTER_VERSION/node_exporter-$NODE_EXPORTER_VERSION.$DIST_ARCH.tar.gz
\  
&& tar xvfz node_exporter-$NODE_EXPORTER_VERSION.$DIST_ARCH.tar.gz \  
&& rm node_exporter-$NODE_EXPORTER_VERSION.$DIST_ARCH.tar.gz  
  
COPY config/prometheus/ /etc/config  
  
# Set app working directory  
WORKDIR /usr/src/app  
  
# Only allow public-key based ssh login  
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
  
# Copy requirements first for better cache on later pushes  
COPY ./requirements/rpi.txt /requirements.txt  
  
# pip install python deps from requirements.txt on the resin.io build server  
RUN pip install -r /requirements.txt  
  
# This will copy all files in our root to the working directory in the
container  
COPY . ./  
  
# Switch on systemd init system in container  
ENV INITSYSTEM on  
  
# make run_on_rpi will run when container starts up on the device  
CMD ["make","run_on_rpi"]  

