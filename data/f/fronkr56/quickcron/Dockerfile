FROM python:2.7  
MAINTAINER Hamilton Turner <hamiltont@gmail.com>  
  
# Need hg to download devcron  
RUN apt-get update && apt-get install -y mercurial ssh sshpass  
  
# Yay devcron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
  
# Setup defaults  
RUN mkdir /cron  
  
VOLUME ["/cron"]  
  
CMD ["devcron.py", "/cron/crontab"]  

