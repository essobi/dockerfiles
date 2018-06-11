#\-------------------------------------------------------  
#  
# Dockerfile for building a simulator driver weewx system  
#  
# build via 'docker build -t weebuntu'  
#  
# run via 'docker -p 22 -p 80 run -t weebuntu'  
# and optionally add -d to run detached in the backgroud  
# or optionally add -t -i to monitor it in the foreground  
#  
# or 'docker run -i -t weebuntu /bin/bash'  
# and in the shell 'service start' nginx and weewx  
#  
# this Dockerfile sets root's password = root  
# and permits root logins over ssh for debugging  
#  
# last modified:  
# 2017-1007 - update to 3.7.1  
# 2016-1008 - update to 3.6.0, use vanila debian image  
# 2016-0505 - update to 3.5.0  
# 2015-1211 - install pyephem, refactor to reduce layers  
# 2015-1206 - update to 3.3.1  
# 2015-0220 vinceskahan@gmail.com - original  
#  
#\-------------------------------------------------------  
  
###FROM debian  
FROM debian:latest  
MAINTAINER Vince Skahan "vinceskahan@gmail.com"  
EXPOSE 22  
EXPOSE 80  
  
# DANGER WILL ROBINSON !!!!  
# set root's password to something trivial  
RUN echo "root:root" | chpasswd  
  
#\---- uncomment to set your timezone to other than UTC  
RUN TIMEZONE="US/Pacific" && echo $TIMEZONE > /etc/timezone && dpkg-
reconfigure --frontend noninteractive tzdata  
  
# sshd needs its /var/run tree there to successfully start up  
RUN mkdir -p /var/run/sshd  
  
# this slows things down a lot - perhaps comment out ?  
RUN apt-get update  
  
# copy supervisor config file into place  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# install misc packages, webserver, weewx prerequisites, pip, supervisord/sshd  
# then install pyephem via pip  
# then install weewx via the setup.py method  
# \- the 'cd' below expects Tom to stick with the weewx-VERSION naming in his
.tgz  
RUN apt-get install -y sqlite3 wget curl procps \  
nginx \  
python-configobj python-cheetah python-imaging python-serial python-usb
python-dev \  
python-pip \  
supervisor openssh-server \  
&& pip install pyephem \  
&& wget http://weewx.com/downloads/weewx-3.7.1.tar.gz -O /tmp/weewx.tgz && \  
cd /tmp && \  
tar zxvf /tmp/weewx.tgz && \  
cd weewx-* ; ./setup.py build ; ./setup.py install --no-prompt && \  
ln -s /var/www/html /home/weewx/public_html && \  
cp /home/weewx/util/init.d/weewx.debian /etc/init.d/weewx  
  
# call supervisord as our container process to run  
CMD ["/usr/bin/supervisord"]  
  
# or use bash instead (and manually run supervisord) for debugging  
# CMD ["/bin/bash"]  

