FROM ubuntu:xenial-20160331.1  
MAINTAINER "Tonybearpan" <tonybearpan@gmail.com>  
ENV UBUNTU_FLAVOR="xenial" \  
UBUNTU_DATE="20160331.1"  
ENV DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu ${UBUNTU_FLAVOR} main
universe\n" > /etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu ${UBUNTU_FLAVOR}-updates main
universe\n" >> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu ${UBUNTU_FLAVOR}-security main
universe\n" >> /etc/apt/sources.list  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
openjdk-8-jre-headless \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
#==============================  
# Locale and encoding settings  
#==============================  
# TODO: Allow to change instance language OS and Browser level  
# see if this helps: https://github.com/rogaha/docker-
desktop/blob/68d7ca9df47b98f3ba58184c951e49098024dc24/Dockerfile#L57  
ENV LANG_WHICH zh  
ENV LANG_WHERE CN  
ENV ENCODING UTF-8  
ENV LANGUAGE ${LANG_WHICH}_${LANG_WHERE}.${ENCODING}  
ENV LANG ${LANGUAGE}  
RUN locale-gen ${LANGUAGE} \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
language-pack-${LANG_WHICH}-hans  
RUN apt-get install fonts-arphic-uming*  
  
#===================  
# Timezone settings  
#===================  
ENV TZ "Asia/Shanghai"  
RUN echo "Setting time zone to '${TZ}'" \  
&& echo ${TZ} > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
LABEL name="Docker image for the Robot Framework http://robotframework.org/"  
LABEL usage="docker run -e ROBOT_TESTS=/path/to/tests/ --rm -v
$(pwd)/path/to/tests/:/path/to/tests/ -ti robot-docker"  
  
#==============================  
# Install Python Pip and the Robot framework  
#==============================  
RUN apt-get update -y  
  
RUN apt-get install -y \  
build-essential \  
fonts-liberation \  
gconf-service \  
libappindicator1 \  
libasound2 \  
libcurl3 \  
libffi-dev \  
libgconf-2-4 \  
libindicator7 \  
libnspr4 \  
libnss3 \  
libpango1.0-0 \  
libssl-dev \  
libxss1 \  
python-dev \  
python-pip \  
python-pyasn1 \  
python-pyasn1-modules \  
unzip \  
wget \  
xdg-utils \  
xvfb \  
python-mysqldb \  
build-essential \  
libmysqlclient-dev \  
&& \  
pip install --upgrade pip  
  
ADD requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt

