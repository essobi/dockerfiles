FROM ubuntu:14.04  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN update-locale  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y build-essential rng-tools  
RUN apt-get install -y python-dev g++ libjpeg-dev sqlite3 openssl  
RUN apt-get install -y alien libssl-dev wget lintian libjs-jquery curl  
  
#  
# install pip from source.  
# workaround https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1363642  
# and
https://github.com/OpenBazaar/OpenBazaar/commit/224f12a371d4eaa36ee7955930c60704e31d61d9  
#  
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py
| sudo python2.7  
  
ADD ./requirements.txt /bazaar/  
RUN cd /bazaar && pip install -r requirements.txt  
  
ADD . /bazaar  
  
ENV LOGNAME openbazaar  
ENV RUNSH_ARGS -q 8888 -p 12345  
WORKDIR /bazaar  
  
ENV LOG_PATH /bazaar/logs/production.log  
  
# touch log file before bash openbazaar to keep tail -f work  
RUN mkdir -p /bazaar/logs && touch $LOG_PATH  
CMD IP=$(/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print
$1}') && \  
bash openbazaar --disable-open-browser -k $IP $RUNSH_ARGS start && tail -f
$LOG_PATH  
  
# clean tmp file  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

