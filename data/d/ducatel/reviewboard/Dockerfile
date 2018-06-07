FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y python-pip python-dev python-svn python-mysqldb libssl-dev
libffi-dev uwsgi libpq-dev wget uwsgi-plugin-python && \  
pip install --upgrade pip && \  
pip install -U pip setuptools cryptography python-memcached psycopg2 &&\  
pip install -U ReviewBoard RBTools && \  
apt-get clean && \  
wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-
linux-amd64-v0.2.0.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz && \  
rm dockerize-linux-amd64-v0.2.0.tar.gz  
  
COPY uwsgi.ini /etc/reviewboard/uwsgi.ini  
COPY run.sh /etc/reviewboard/run.sh  
RUN chmod +x /etc/reviewboard/run.sh  
  
ENV DB_TYPE mysql  
ENV DB_PORT 3306  
ENV DB_NAME reviewboard  
ENV DB_USER reviewboard  
ENV DB_PASSWORD reviewboard  
ENV RB_ADMIN admin  
ENV RB_PASSWORD admin  
ENV RB_ADMIN_EMAIL admin@example.com  
ENV UWSGI_PROCESSES 10  
VOLUME "/media"  
VOLUME "/var/www"  
EXPOSE 8000  
CMD ["/etc/reviewboard/run.sh"]  

