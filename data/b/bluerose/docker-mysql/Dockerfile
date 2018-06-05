FROM mysql  
  
ENV S3CMD_VERSION 1.6.1  
ENV DOCKERIZE_VERSION v0.6.0  
RUN apt-get update && \  
apt-get install -y \  
cron \  
less \  
python-setuptools \  
supervisor \  
vim \  
wget && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
wget
https://github.com/s3tools/s3cmd/releases/download/v${S3CMD_VERSION}/s3cmd-${S3CMD_VERSION}.tar.gz
&& \  
tar xzf s3cmd-${S3CMD_VERSION}.tar.gz && \  
cd s3cmd-${S3CMD_VERSION} && \  
python setup.py install  
  
ADD ./.s3cfg.tmpl /root/.s3cfg.tmpl  
  
# backup script  
ADD ./mysqltos3.sh /usr/local/bin/mysqltos3  
ADD ./mysqld.sh /usr/local/bin/mysqld.sh  
ADD ./env_secrets_expand.sh /usr/local/bin/env_secrets_expand.sh  
ADD ./shutdown-hook.sh /usr/local/bin/shutdown-hook.sh  
  
RUN rm /entrypoint.sh  
ADD ./entrypoint.sh /entrypoint.sh  
  
ADD ./supervisord/* /etc/supervisor/conf.d/  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord", "-n"]  
  

