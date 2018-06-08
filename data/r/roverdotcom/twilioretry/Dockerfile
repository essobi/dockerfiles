FROM ubuntu:14.04  
RUN apt-get update -q  
RUN apt-get install -y supervisor python-pip python-virtualenv mercurial
openssh-server  
  
# Yay devcron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
RUN mkdir /cron  
COPY docker/crontab /cron/crontab  
  
# Supervisord  
RUN mkdir -p /var/log/supervisor  
COPY docker/supervisord.conf /etc/supervisor/supervisord.conf  
  
# Twilioretry  
RUN mkdir /twilioretry  
RUN virtualenv /twilioretry/venv  
COPY requirements.txt /twilioretry/requirements.txt  
RUN /twilioretry/venv/bin/pip install -r /twilioretry/requirements.txt  
COPY . /twilioretry  
  
EXPOSE 5000  
VOLUME /twilioretry/stored-requests/  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

