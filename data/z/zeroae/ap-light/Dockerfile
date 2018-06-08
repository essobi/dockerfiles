FROM debian:jessie  
MAINTAINER Patrick Sodré <sodre@zeroae.co>  
  
ENV AP_ROOT="/opt/ap"  
ENV \  
AP_SERVICE_DIR="${AP_ROOT}/service" \  
AP_STATE_DIR="${AP_ROOT}/run/state" \  
PATH=${AP_ROOT}/bin:${PATH} \  
CONTAINERPILOT="file:///etc/containerpilot.json"  
ADD file ${AP_ROOT}/file  
ADD bin ${AP_ROOT}/bin  
  
ADD build.sh ${AP_ROOT}/build.sh  
RUN /opt/ap/build.sh  
  
ADD service-available ${AP_ROOT}/service-available  
  
RUN ap-service-add :containerpilot  
  
VOLUME [ "/var/lib/consul", "${AP_STATE_DIR}" ]  
  
CMD [ "containerpilot", "ap-spin"]  

