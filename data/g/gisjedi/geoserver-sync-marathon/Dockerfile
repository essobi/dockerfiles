FROM hmtisr/centos:7-gosu  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \  
&& python get-pip.py \  
&& rm get-pip.py  
  
COPY requirements.txt /  
RUN pip install -r requirements.txt  
  
RUN mkdir -p /opt/gs-sync  
  
COPY . /opt/gs-sync/  
RUN chmod +x /opt/gs-sync/*.py \  
&& chmod +x /opt/gs-sync/*.sh  
  
# Environment variables that can be specified to override setting defaults:  
#GEOSERVER_DATA_DIR: file system location to watch for updates  
#GS_RELOAD_INTERVAL: time in seconds between reload of each slave instance  
#GS_PROTOCOL: protocol prefix, should be set to 'http' or 'https'  
#GS_RELATIVE_URL: relative URL to GeoServer REST API  
#GOSU_USER: User ID and group ID (user:group) ownership of GeoServer
configuration storage.  
#MARATHON_ROOT_URL: protocal, address or ip and port to Marathon (default of
http://marathon.mesos:8080)  
#MARATHON_APP: app name within Marathon used to group all tasks (server
instances)  
#MARATHON_APP_PORT: internal port of service (internal to docker container:
default of 8080)  
#POLLING_INTERVAL: interval between polling the file system for updates  
#FILE_BLACKLIST: comma delimited list of files to ignore during file system
polling (.log)  
  
# GeoServer package pass-through settings:  
#FRAMEWORK_NAME: (defaults to GeoServer)  
#GS_SLAVE_INSTANCES: defaults to 3  
#HOST_GEOSERVER_DATA_DIR: location the GeoServer data directory resides on the
host (defaults to /shared/geoserver)  
EXPOSE 8000  
  
WORKDIR /opt/gs-sync  
CMD ["./wrapper.sh"]  

