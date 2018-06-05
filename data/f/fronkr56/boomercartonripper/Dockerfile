FROM python:2.7  
MAINTAINER Ryan Fronk <fronkr56@gmail.com>  
RUN apt-get update && apt-get install -y mercurial streamripper  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
RUN mkdir /cron /mnt/Audio /tmp/Streamripper  
ADD start.sh /cron/start.sh  
RUN echo "0 5 * * 1 /bin/bash /cron/start.sh" > /cron/crontab && \  
echo "0 5 * * 2 /bin/bash /cron/start.sh" >> /cron/crontab && \  
echo "0 5 * * 3 /bin/bash /cron/start.sh" >> /cron/crontab && \  
echo "0 5 * * 4 /bin/bash /cron/start.sh" >> /cron/crontab && \  
echo "0 5 * * 5 /bin/bash /cron/start.sh" >> /cron/crontab && \  
chmod a+x /cron/start.sh  
VOLUME ["/cron", "/mnt/Audio"]  
CMD ["devcron.py", "/cron/crontab"]  

