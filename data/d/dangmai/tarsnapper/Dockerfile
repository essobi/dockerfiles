FROM atmoz/tarsnap  
LABEL maintainer="Dang Mai <contact@dangmai.net>"  
  
ENV TARSNAPPER_VERSION 0.4.0  
RUN apt-get -q update && apt-get install -qy \  
python-pip \  
cron \  
&& pip install tarsnapper==$TARSNAPPER_VERSION -i
https://pypi.python.org/simple \  
&& apt-get autoremove -y \  
&& apt-get clean all \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD tarsnapper.conf /etc/tarsnapper.conf  
ADD tarsnapper-backup.sh /tarsnapper-backup.sh  
ADD start.sh /start.sh  
RUN chmod u+x /tarsnapper-backup.sh /start.sh  
  
CMD /start.sh  

