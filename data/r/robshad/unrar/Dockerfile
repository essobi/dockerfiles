FROM linuxserver/baseimage  
MAINTAINER Rob Shad <robertmshad@googlemail.com>  
ENV APTLIST="cron lftp wget"  
RUN apt-get update -q && \  
apt-get install $APTLIST -qy && \  
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
ADD scripts/ /scripts/  
RUN rm -f /tmp/autounrar.pid  
RUN echo "Setting file permissions"  
RUN chmod -v +x /scripts/autounrar  
RUN echo "Adding cron job"  
RUN crontab -l | { cat; echo "*/5 * * * * /scripts/autounrar"; } | crontab -  
  
# Volumes and Ports  
VOLUME ["/input", "/output", "/config"]  

