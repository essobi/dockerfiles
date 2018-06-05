FROM ubuntu:14.04  
# Locales  
RUN (apt-get clean \  
&& apt-key update \  
&& apt-get -q -y update --fix-missing \  
&& apt-get -q -y update \  
&& apt-get install -q -y apt-utils \  
&& apt-get install -q -y locales) && \  
rm -rf /var/lib/apt/lists/*  
  
ADD conf/locale.gen /etc/locale.gen  
RUN (locale-gen \  
&& locale-gen es_ES.UTF-8 \  
&& dpkg-reconfigure locales)  
  
ENV LANGUAGE es_ES.UTF-8  
ENV LANG es_ES.UTF-8  
ENV LC_ALL es_ES.UTF-8  
ENV LC_CTYPE es_ES.UTF-8  
# python  
RUN apt-get update && \  
apt-get install -y \  
python3 python3-pip libpq-dev libjpeg-dev python-dev \  
libmysqlclient-dev software-properties-common && \  
rm -rf /var/lib/apt/lists/*  
# ffmpeg  
RUN add-apt-repository ppa:mc3man/trusty-media -y  
RUN apt-get update && \  
apt-get install -y ffmpeg vorbis-tools flac lame && \  
rm -rf /var/lib/apt/lists/*  
# git  
RUN apt-get update && \  
apt-get install -y git && \  
rm -rf /var/lib/apt/lists/*  
# nodejs  
RUN apt-get update && \  
apt-get install -y nodejs npm && \  
rm -rf /var/lib/apt/lists/*  
# collectstatic dependencies  
RUN npm install -g bower less yuglify  
  
# fix node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
ADD ./requirements.txt /usr/src/app/  
  
WORKDIR /usr/src/app  
RUN pip3 install -r requirements.txt  
  
ADD . /usr/src/app  
  
CMD ["/usr/local/bin/gunicorn", "sharemusic.wsgi:application", "-b :8000", "-w
6", "-t 5000"]  

