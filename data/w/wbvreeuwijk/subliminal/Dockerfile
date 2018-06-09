# Subliminal  
#  
# Version 0.1  
FROM wbvreeuwijk/nzb-base:latest  
MAINTAINER Bas van Reeuwijk <bas@reeuwijk.net>  
  
LABEL Description="This image will install a Subliminal command environment"
Version="1.0"  
  
# Install subliminal  
RUN cd /opt \  
&& git clone https://github.com/sprt/subliminal.git -b develop \  
&& cd subliminal \  
&& python setup.py install  
  
# Insert schedule in crontab  
RUN echo "0 0,3,9,12,15,18,21 * * * /usr/bin/subliminal download /video/TV -a
4w -l en -l nl -v" >> /etc/crontabs/sabnzbd  
RUN echo "30 0,8,16 * * * /usr/bin/subliminal download /video/Movies -a 4w -l
en -l nl -v" >> /etc/crontabs/sabnzbd  
  
# Directory for video files  
VOLUME ["/video"]  
  
CMD ["crond", "-f", "-d", "8"]  
  

