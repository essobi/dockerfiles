FROM ubuntu:xenial  
  
MAINTAINER MrUPGrade itsupgradetime@gmail.com  
  
ADD ./get-pip.py /  
  
RUN apt-get purge -y python.* && \  
echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu xenial main" >>
/etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu xenial main"
>> /etc/apt/sources.list && \  
apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys
FF3997E83CD969B409FB24BC5BB92C09DB82666C && \  
apt-get update && \  
apt-get install -y python3.3 && \  
python3.3 /get-pip.py && \  
pip install \--upgrade pip && \  
ln -s /usr/bin/python3.3 /usr/bin/python && \  
rm -f /get-pip.py && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["python"]  

