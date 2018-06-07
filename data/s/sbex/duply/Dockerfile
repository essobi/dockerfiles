#FROM ubuntu:16.04  
FROM python:2.7  
MAINTAINER greg@bity.com  
  
# Duply  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
duply \  
ncftp \  
pwgen \  
sshfs \  
python-boto \  
python-pip \  
git \  
curl \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
#RUN pip install -U setuptools  
#RUN pip install --upgrade s3cmd  
#RUN pip install boto  
#RUN apt-get update && apt-get install -y python-setuptools  
ENV HOME /root  
  
# Tahoe  
RUN git clone https://github.com/tahoe-lafs/tahoe-lafs.git tahoe-lafs && \  
cd /tahoe-lafs && \  
git pull --depth=100 && \  
pip install . && \  
rm -rf ~/.cache/  
  
#RUN apt-get update && apt-get install -y build-essential python2.7-dev
libffi-dev libssl-dev python-virtualenv  
#RUN apt-get update && apt-get install -y tahoe-lafs  
#&& apt-get install -y python-cffi --reinstall  
RUN tahoe --version  
  
#For backup to S3  
#ENV AWS_ACCESS_KEY_ID w_fdfd...  
#ENV AWS_SECRET_ACCESS_KEY X_h...  
#expose 3456  
WORKDIR /root  
  
#COPY files/entrypoint.sh /entrypoint.sh  
#ENTRYPOINT ["/entrypoint.sh"]  
CMD [ "tahoe", "start", ".tahoe/", "--nodaemon", "--logfile=-" ]  
#CMD /usr/local/bin/tahoe start /root/.tahoe/ -n --pidfile /root/twistd.pid  
#CMD tahoe start  

