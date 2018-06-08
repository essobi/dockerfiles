FROM debian:wheezy  
MAINTAINER ncg09@hampshire.edu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY start.sh /  
COPY uwsgi.ini /  
COPY shell.sh /  
  
RUN apt-get update \  
&& apt-get install -y \  
git-core \  
patch \  
python-dev \  
python-mysqldb \  
python-pip \  
python-setuptools \  
python-subvertpy \  
memcached \  
python-svn \  
subversion \  
&& easy_install reviewboard \  
&& pip install -U uwsgi \  
&& chmod +x /start.sh /shell.sh  
  
VOLUME ["/.ssh", "/media/"]  
  
EXPOSE 8000  
CMD /start.sh  

