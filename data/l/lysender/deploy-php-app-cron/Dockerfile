FROM lysender/php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN yum -y install pwgen \  
python \  
python-devel \  
python-pip \  
mercurial && yum clean all  
  
# Install dev cron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron  
  
# Configure servicies  
ADD ./cron.conf /cron/crontab  
ADD ./deploy.sh /deploy.sh  
RUN chmod 0775 /deploy.sh  
RUN mkdir -p /var/log/deploy-agent  
  
VOLUME ["/cron", "/var/www/html", "/root/.ssh", "/var/log/deploy-agent"]  
  
CMD ["devcron.py", "/cron/crontab"]  
  

