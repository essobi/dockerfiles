FROM jsurf/rpi-java  
  
RUN [ "cross-build-start" ]  
  
ENV LANG C.UTF-8  
ENV TZ Europe/Berlin  
  
# Boinc, from laurentmalvert/docker-boinc  
RUN apt-get update && \  
apt-get -q install -y boinc-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN [ "cross-build-end" ]  
  
EXPOSE \  
31416 \  
80 \  
443  
# default environment variables  
ENV ROLE = client  
ENV CENTRAL_HUB_IP = localhost  
  
# eden314  
wget
https://circleci.com/api/v1/project/thombohlk/GrowPi/latest/artifacts/0/$CIRCLE_ARTIFACTS/GrowPi-0.1.jar  
  
# start  
ENTRYPOINT ["sudo", "./start.sh", $role, $central_hub_ip, $project_url,
$project_auth]

