FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV WATCHERS 16384  
RUN apt-get update -y  
  
# Install duplicity and tools to monitor file changes  
RUN apt-get update -y \  
&& \  
apt-get install -y \  
wget python python-dev python-pip librsync-dev \  
ncftp lftp rsync software-properties-common \  
ntpdate inotify-tools \  
&& \  
add-apt-repository -y ppa:duplicity-team/ppa \  
&& \  
apt-get update -y \  
&& \  
apt-get install -y duplicity \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Install all required python libs for s3  
ADD requirements.txt /opt/  
RUN pip install --upgrade --requirement /opt/requirements.txt  
  
ADD ./run.sh /run.sh  
CMD ["/run.sh"]  

