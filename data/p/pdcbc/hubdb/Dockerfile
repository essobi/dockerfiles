# Dockerfile for the HDC's ComposerDb service  
#  
#  
# HubDB for HDC-collected aggregate data.  
#  
# Example:  
# sudo docker pull healthDataCoalition/composerDb  
# sudo docker run -d --name composerDb -h composerDb --restart=always \  
# -v /path/for/composerDb/:/data/:rw \  
# healthDataCoalition/composerDb:latest  
#  
#  
FROM mongo:3.2  
MAINTAINER derek.roberts@gmail.com  
  
  
# Environment variables  
#  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install cron and add it to the existing entrypoint.sh  
#  
RUN apt-get update; \  
apt-get install -y \  
cron; \  
rm -rf /var/lib/apt/lists/*; \  
sed -i 's/set -e/set -e\n\n\n# Start cron\nservice cron start\n/g'
/entrypoint.sh  
  
# Create Mongo maintenance script and add to cron  
#  
RUN SCRIPT=/mongoDump.sh; \  
( \  
echo '#!/bin/bash'; \  
echo ''; \  
echo 'set -e -o nounset'; \  
echo ''; \  
echo ''; \  
echo '# Wait for Mongod to start (important at boot), then dump'; \  
echo 'sleep 30'; \  
echo 'mongodump --out /data/dump/'; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}; \  
( \  
echo '# Run database dump script (boot, 2 PST = 10 UTC)'; \  
echo '@reboot '${SCRIPT}; \  
echo '0 10 * * * '${SCRIPT}; \  
) \  
| crontab -  
  
# Volume  
#  
RUN mkdir -p /data/dump/  
VOLUME /data/dump/  

