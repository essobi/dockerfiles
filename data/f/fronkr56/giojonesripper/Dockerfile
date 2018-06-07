FROM python:2.7  
MAINTAINER Ryan Fronk <fronkr56@gmail.com>  
RUN apt-get update && apt-get install -y mercurial streamripper  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
RUN mkdir /cron /mnt/Audio /tmp/Streamripper  
ADD start.sh /cron/start.sh  
RUN echo "0 6 * * 1 /cron/start.sh" > /cron/crontab && \  
echo "0 6 * * 2 /cron/start.sh" >> /cron/crontab && \  
echo "0 6 * * 3 /cron/start.sh" >> /cron/crontab && \  
echo "0 6 * * 4 /cron/start.sh" >> /cron/crontab && \  
echo "0 6 * * 5 /cron/start.sh" >> /cron/crontab && \  
chmod a+x /cron/start.sh  
VOLUME ["/cron", "/mnt/Audio"]  
CMD ["devcron.py", "/cron/crontab"]  

