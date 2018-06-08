FROM ubuntu:14.04  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN apt-get update && apt-get install -y build-essential  
RUN apt-get install -y python2.7 python2.7-dev python-pip  
RUN apt-get install -y libsasl2-dev libxml2-dev libxslt-dev libpq-dev
libldap2-dev  
  
RUN apt-get install -y supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/  
  
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user  
WORKDIR /home/user  
  
RUN pip install psycopg2 redis hiredis nydus  
  
ENV SENTRY_VERSION 7.1.4  
RUN pip install sentry==$SENTRY_VERSION  
  
# install plugins  
ENV SENTRY_SLACK_VERSION 0.2.0  
RUN pip install sentry-slack==$SENTRY_SLACK_VERSION  
  
ADD sentry.conf.py /home/user/.sentry/  
RUN chown -R user:user /home/user/.sentry # TODO this might not work on AUFS
sometimes  
RUN chown -R user:user /var/log/supervisor  
  
USER user  
EXPOSE 9000  
CMD ["/usr/bin/supervisord"]  

