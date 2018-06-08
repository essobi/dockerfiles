FROM ubuntu  
MAINTAINER rakai93  
  
# install sentry  
WORKDIR /tmp  
RUN \  
# install python, pip, other dependencies and sentry \  
\  
apt-get update && apt-get install -y build-essential curl python python-dev
libxml2-dev libxslt-dev libffi-dev libssl-dev postgresql postgresql-contrib
libpq-dev && \  
curl -s https://bootstrap.pypa.io/get-pip.py | python && \  
pip install -U sentry[postgres] && \  
\  
# install supervisor to manage tasks \  
\  
pip install -U supervisor  
  
# add config  
ADD sentry.conf.py /etc/sentry.conf.py  
ENV SENTRY_CONF=/etc/sentry.conf.py  
ADD supervisord.conf /etc/supervisord.conf  
  
# run startup script  
ADD run-sentry.sh /run-sentry  
RUN chmod o+x /run-sentry  
WORKDIR /root  
CMD ["/run-sentry"]  

