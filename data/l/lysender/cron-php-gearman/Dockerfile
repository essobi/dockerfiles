FROM lysender/php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN yum -y install libevent \  
gearmand \  
libgearman \  
libgearman-devel \  
php-pecl-gearman \  
python \  
python-devel \  
python-pip \  
mercurial && yum clean all  
  
# Install dev cron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
  
# Configure servicies  
ADD ./cron.conf /cron/crontab  
  
VOLUME ["/cron"]  
  
CMD ["devcron.py", "/cron/crontab"]  
  

