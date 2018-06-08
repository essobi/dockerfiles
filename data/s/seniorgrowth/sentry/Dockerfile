FROM sentry:8.4  
  
RUN apt-get update &&\  
apt-get -y install libjpeg-dev &&\  
pip install --upgrade \  
https://github.com/getsentry/sentry-auth-github/archive/master.zip \  
sentry-github &&\  
apt-get autoremove -y &&\  
apt-get clean  
  
  
COPY seniorgrowth.conf.py /etc/sentry/sentry.conf.py  

