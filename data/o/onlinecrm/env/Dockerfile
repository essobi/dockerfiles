FROM selenium/standalone-chrome  
  
USER root  
  
RUN locale-gen zh_TW.UTF-8 zh_CN.UTF-8 en_US.UTF-8  
ENV LANG='zh_TW.UTF-8' \  
LANGUAGE='zh_TW.UTF-8' \  
LC_CTYPE='zh_TW.UTF-8' \  
LC_NUMERIC='zh_TW.UTF-8' \  
LC_TIME='zh_TW.UTF-8' \  
LC_COLLATE='zh_TW.UTF-8' \  
LC_MONETARY='zh_TW.UTF-8' \  
LC_MESSAGES='zh_TW.UTF-8' \  
LC_PAPER='zh_TW.UTF-8' \  
LC_NAME='zh_TW.UTF-8' \  
LC_ADDRESS='zh_TW.UTF-8' \  
LC_TELEPHONE='zh_TW.UTF-8' \  
LC_MEASUREMENT='zh_TW.UTF-8' \  
LC_IDENTIFICATION='zh_TW.UTF-8'\  
LC_ALL='zh_TW.UTF-8'  
RUN apt-get -y update  
RUN apt-get -y install \  
python-dev \  
python3-pip \  
libjpeg-dev \  
zlib1g-dev \  
libpq-dev \  
git \  
unzip \  
xvfb \  
libnss3 \  
libnss3-dev \  
libgconf-2-4 \  
groff \  
curl \  
cloud-utils  
  
RUN pip3 install --upgrade pip  
RUN pip3 install \  
ipython \  
awscli \  
boto3 \  
psycopg2 \  
SQLAlchemy \  
requests \  
selenium \  
BeautifulSoup4 \  
pyvirtualdisplay \  
pyyaml \  
Pillow \  
cryptography  
  
  
USER  seluser  

