###### QNIBTerminal Image  
FROM qnib/terminal:fd22  
  
  
# Inspired from the official docker image  
# > https://github.com/getsentry/docker-
sentry/blob/3115587c614e64c66419a26b4f7be6ac067e3a79/Dockerfile  
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user  
WORKDIR /home/user  
  
# If you change this, you'll also need to install the appropriate python  
# package:  
RUN dnf install -y postgresql-devel && \  
pip install psycopg2  
RUN dnf install -y mysql-devel && \  
pip install mysql-python  
  
# You'll need to install the required dependencies for Memcached:  
RUN pip install python-memcached  
  
# You'll need to install the required dependencies for Redis buffers:  
RUN pip install redis hiredis nydus  
  
ENV SENTRY_VERSION 7.7.0  
RUN dnf install -y libxslt-devel libxml-devel libffi-devel && \  
pip install sentry==$SENTRY_VERSION  
  
#### Dependencies which should be carved out later  
# REDIS  
RUN dnf install -y redis  
#### END  
RUN mkdir -p /home/user/.sentry \  
&& chown -R user:user /home/user/.sentry  
ADD sentry/sentry.conf.py /home/user/.sentry/sentry.conf.py  
ADD etc/supervisord.d/*.ini /etc/supervisord.d/  
ADD opt/qnib/sentry/bin/start_* /opt/qnib/sentry/bin/  
ADD etc/consul.d/*.json /etc/consul.d/  
ADD sentry/sentry.db /home/user/.sentry/sentry.db  
RUN chown user: /home/user/.sentry/sentry.db  

