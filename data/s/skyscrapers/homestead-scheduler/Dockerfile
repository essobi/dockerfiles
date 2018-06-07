FROM ubuntu:14.04  
MAINTAINER skyscrapers "support@skyscrapers.eu"  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.10.0  
ENV DOCKER_SHA256
a66b20423b7d849aa8ef448b98b41d18c45a30bf3fe952cc2ba4760600b18087  
  
RUN apt-get install -y curl  
RUN curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION" -o
/usr/local/bin/docker \  
&& echo "${DOCKER_SHA256} /usr/local/bin/docker" | sha256sum -c - \  
&& chmod +x /usr/local/bin/docker  
  
# Add crontab file in the cron directory  
ADD cron.d /etc/cron.d/  
ADD scripts /etc/scheduler/  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/homestead-cron && \  
chmod 0755 /etc/scheduler/*  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Run the command on container startup  
CMD /etc/scheduler/run-scheduler.sh

