from ubuntu:trusty  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
ENV REFRESHED_AT 2014-07-07  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN sed 's/us-east-1.ec2.archive.ubuntu.com/nova.clouds.archive.ubuntu.com/'
-i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
RUN apt-get update  
  
RUN apt-get install -y build-essential \  
c++-4.7 \  
git \  
g++-4.7 \  
npm \  
python-matplotlib \  
python-mysqldb \  
python-numpy \  
python-scipy \  
python-setuptools  
RUN easy_install pip  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install tty.js  
  
# sets root password to password, but isn't accessible from the outside  
RUN echo 'mysql-server-5.5 mysql-server/root_password password password' |
debconf-set-selections  
RUN echo 'mysql-server-5.5 mysql-server/root_password_again password password'
| debconf-set-selections  
RUN apt-get update && apt-get install -y mysql-server && apt-get clean && rm
-rf /var/lib/apt/lists/*  
  
ENV REDWOOD_PULLED_AT 2014-06-24  
RUN git clone https://github.com/Lab41/Redwood.git  
ADD visual.py /Redwood/redwood/helpers/visual.py  
ADD redwood /Redwood/bin/redwood  
RUN rm -rf /Redwood/Filters/file_types.py  
RUN mkdir /Redwood/mysql  
RUN mkdir -p /Redwood/reports/output/reports  
RUN mv /Redwood/reports/resources /Redwood/reports/output/reports/resources  
RUN cd /Redwood; python setup.py install  
  
ADD . /src  
  
ADD favicon.ico /node_modules/tty.js/static/favicon.ico  
ADD index.html /node_modules/tty.js/static/index.html  
ADD tty.js /node_modules/tty.js/bin/tty.js  
  
# add rsyslog  
RUN sed 's/#\$ModLoad imudp/\$ModLoad imudp/' -i /etc/rsyslog.conf  
RUN sed 's/#\$UDPServerRun 514/\$UDPServerRun 514/' -i /etc/rsyslog.conf  
  
# use non root user  
RUN touch /etc/rsyslog.d/50-default.conf  
RUN echo "mysql ALL=NOPASSWD: /etc/init.d/rsyslog start" >> /etc/sudoers  
RUN chown -R mysql /Redwood /src /node_modules/tty.js
/etc/rsyslog.d/50-default.conf  
  
USER mysql  
  
EXPOSE 8000  
CMD printf "*.*\t@$REMOTE_HOST" >> /etc/rsyslog.d/50-default.conf; \  
sudo /etc/init.d/rsyslog start; \  
logger started redwood container $PARENT_HOST; \  
/src/startup.sh  

