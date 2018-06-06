FROM ubuntu:14.04  
MAINTAINER mithro@mithis.com  
RUN apt-get -y update  
  
# Make sure the keyrings are up to date  
RUN apt-get -y install add-apt-key ubuntu-keyring ubuntu-extras-keyring  
# Get us closer to the travis environment  
RUN apt-get -y install locales && locale-gen en_US en_US.UTF-8 && dpkg-
reconfigure locales  
RUN sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list  
  
# Update / upgrade everything  
RUN apt-get -y update && apt-get -y upgrade  
  
# gst-switch compile stuff  
RUN apt-get -y install build-essential dh-autoreconf  
RUN apt-get -y install libgtk-3-dev  
RUN apt-get -y install gstreamer1.0.* libgstreamer.*1.0.*  
  
# Python stuff for gst-switch API - Python 2.7  
RUN apt-get -y install python-software-properties python-pip  
RUN apt-get -y install libglib2.0-dev gir1.2-glib-2.0 libgirepository1.0-dev
libglib2.0-0 python-gi  
RUN apt-get -y install python-scipy  
RUN pip install mock --upgrade  
RUN pip install pytest-cov --upgrade  
RUN pip install pytest-pep8 --upgrade  
RUN pip install pylint --upgrade  
  
# Python stuff for gst-switch API - Python 3.4  
RUN apt-get -y install python3-software-properties python3-pip  
RUN apt-get -y install libglib2.0-dev gir1.2-glib-2.0 libgirepository1.0-dev
libglib2.0-0 python3-gi  
RUN apt-get -y install python3-scipy  
RUN pip3 install mock --upgrade  
RUN pip3 install pytest-cov --upgrade  
RUN pip3 install pytest-pep8 --upgrade  
RUN pip3 install pylint --upgrade  
  
# Python stuff for gst-switch API  
RUN apt-get -y install python-software-properties python-pip  
RUN apt-get -y install libglib2.0-dev gir1.2-glib-2.0 libgirepository1.0-dev
libglib2.0-0 python-gi  
RUN apt-get -y install python-scipy  
  
# Needed for tests  
RUN apt-get -y install wget libav-tools  
  
# Tools needed  
RUN apt-get -y install git  
  
# Add the travis user with sudo  
RUN adduser --disabled-password --gecos "" travis  
RUN adduser travis sudo  
  
RUN cat /etc/sudoers  
RUN sed -i -e's/%sudo ALL=(ALL:ALL) ALL/%sudo ALL=(ALL:ALL) NOPASSWD:ALL/'
/etc/sudoers  
  
ADD run.py /run.py  
ADD run-stage2.py /run-stage2.py  
RUN chmod a+rx /run*.py  
  
USER travis  
WORKDIR /home/travis  

