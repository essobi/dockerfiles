FROM python:alpine  
  
RUN apk update \  
&& apk --no-cache add \  
git \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
#
=======================================================================================  
# Install Sentinel  
#
=======================================================================================  
WORKDIR /home/munuser/sentinel  
  
RUN git clone https://github.com/muncrypto/sentinel.git /home/munuser/sentinel
\  
  
&& pip install -r requirements.txt \  
&& echo "mun_conf=/mnt/mun/config/mun.conf" >> sentinel.conf  
  
CMD ["/home/munuser/sentinel/bin/sentinel.py >/dev/null 2>&1"]

