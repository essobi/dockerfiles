FROM ubuntu:14.04  
MAINTAINER Zhong Pei <zhongpei@vip.qq.com>  
  
# keep upstart quiet  
RUN dpkg-divert --local --rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# time zone  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
  
ADD ./requirements /requirements  
# RUN sed -i 's/archive.ubuntu.com/mirrors.163.com/' /etc/apt/sources.list  
RUN apt-get update --fix-missing \  
&& apt-get install -y build-essential git \  
&& apt-get install -y python python-dev python-setuptools python-pip python-
virtualenv \  
&& apt-get install -y --no-install-recommends libxml2-dev libxslt-dev libjpeg-
dev libfreetype6-dev zlib1g-dev libpng12-dev python-imaging libmysqlclient-dev
\  
&& apt-get build-dep -y python-imaging python-psycopg2 \  
&& pip install -r /requirements/base.txt \  
&& pip install supervisor-stdout \  
&& apt-get install -y supervisor\  
&& apt-get install -y mysql-client \  
&& rm -fr ~/.cache/pip \  
&& apt-get -y clean && apt-get -y autoclean  
  
# stop supervisor service as we'll run it manually  
RUN service supervisor stop  
  
# start supervisor to run our wsgi server  
ADD ./supervisord.conf /etc/supervisord.conf  
CMD supervisord -c /etc/supervisord.conf -n  
  
# expose port(s)  
EXPOSE 5000  

