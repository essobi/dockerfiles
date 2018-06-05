FROM ubuntu:14.04  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV GIT_URL_FIGWAY https://github.com/telefonicaid/fiware-figway.git  
ENV GIT_REV_FIGWAY master  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD no  
  
WORKDIR /opt  
  
RUN apt-get update && \  
apt-get -y install --no-install-recommends\  
git \  
ca-certificates \  
acpi \  
python python-requests \  
&& \  
apt-get clean && \  
find /var/lib/apt/lists -type f -delete && \  
git clone ${GIT_URL_FIGWAY} && \  
sed -i /opt/fiware-figway/python-IDAS4/Sensors_UL20/RegisterDevice.py -e
'/PAYLOAD_json\\["devices"\\]\\[0\\]\\["entity_name"\\]=ENTITY_ID/a
PAYLOAD_json["devices"][0]["protocol"]="PDI-IoTA-UltraLight"' && \  
mkdir -p /opt/scripts  
  
WORKDIR /opt/fiware-figway/python-IDAS4  
  
COPY therm-sensors.sh /opt/scripts/  
COPY send-data.sh /opt/scripts/  
  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

