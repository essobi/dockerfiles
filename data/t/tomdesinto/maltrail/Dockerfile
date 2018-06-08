FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y python-pcapy git curl schedtool \  
&& git clone https://github.com/stamparm/maltrail.git /maltrail \  
&& python /maltrail/core/update.py  
  
WORKDIR /maltrail  
VOLUME /var/log/maltrail  
  
COPY maltrail.conf /maltrail/maltrail.conf  
  

