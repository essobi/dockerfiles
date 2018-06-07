FROM debian:wheezy  
MAINTAINER jim.mei@centling.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DOMAIN localhost  
  
  
RUN apt-get update \  
&& apt-get install -y \  
git-core \  
libjpeg8 \  
libfreetype6 \  
libfreetype6-dev \  
patch \  
python-dev \  
python-mysqldb \  
python-pip \  
python-setuptools \  
python-subvertpy \  
memcached \  
python-imaging \  
python-svn \  
subversion \  
libpcre3 libpcre3-dev python-ldap  
  
# Since Reviewboard 2.5 it has a dependency for Pillow.  
# Since Pillow 3.0.0 installation fails if there is no libjpeg library [RFC:
Require libjpeg and zlib by default](https://github.com/python-
pillow/Pillow/issues/1412)  
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
liblcms2-dev libwebp-dev python-tk  
  
RUN easy_install reviewboard  
RUN pip install -U uwsgi  
  
COPY start.sh /  
COPY uwsgi.ini /  
COPY shell.sh /  
RUN chmod +x /start.sh /shell.sh  
  
VOLUME ["/.ssh", "/media/"]  
  
EXPOSE 8000  
# For debugging  
RUN apt-get install -y procps  
RUN apt-get install -y net-tools  
RUN apt-get install -y netcat  
  
CMD /start.sh  

