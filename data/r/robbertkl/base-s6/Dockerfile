FROM robbertkl/base  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
# Install services  
RUN cleaninstall \  
cron \  
rsyslog  
  
# Install s6-overlay  
RUN VERSION=`latestversion just-containers/s6-overlay` \  
&& curl -sSL "https://github.com/just-
containers/s6-overlay/releases/download/v${VERSION}/s6-overlay-amd64.tar.gz" \  
| tar xzf - -C /  
RUN sed -i "s/s6-nuke -th/s6-nuke -t/" /etc/s6/init/init-stage3  
  
# Copy own stuff  
COPY bin /usr/bin  
COPY etc /etc  
  
# Configure services  
RUN touch /var/log/messages \  
&& chmod 600 /etc/crontab \  
&& rm -f /etc/cron.daily/apt /etc/cron.daily/dpkg /etc/cron.daily/passwd  
  
# Run s6 service supervisor (not as entrypoint!)  
CMD [ "/init" ]  

