from ubuntu:14.04  
MAINTAINER George.li  
  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
  
RUN apt-get update  
RUN apt-get install -y build-essential libssl-dev  
RUN apt-get install -y nodejs  
RUN apt-get install -y python-software-properties python  
RUN apt-get install -y git  
RUN apt-get -y install python-setuptools  
RUN apt-get install -y python-dev  
RUN apt-get install -y libmysqlclient-dev  
RUN apt-get install -y libxml2-dev libxslt1-dev libxslt-dev  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y build-essential libssl-dev libffi-dev  
RUN npm install -g browserify  
RUN easy_install pip  
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk  
RUN npm -g install npm@2.1.1  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
RUN apt-get install -y uwsgi  
RUN locale-gen zh_TW zh_TW.UTF-8 zh_CN.UTF-8 en_US.UTF-8  
ENV LC_CTYPE=zh_TW.UTF-8  
ENV LC_MESSAGES=zh_TW.UTF-8  
ENV LC_TIME=en_US.UTF-8  
RUN apt-get install -y unzip  
ADD google_appengine_1.9.30.zip /tmp/google_appengine.zip  
RUN unzip /tmp/google_appengine.zip -d /usr/lib  
  

