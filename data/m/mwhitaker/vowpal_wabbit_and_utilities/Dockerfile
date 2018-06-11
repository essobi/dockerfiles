FROM ubuntu:14.04  
MAINTAINER Michael Whitaker  
  
RUN apt-get update  
  
RUN apt-get -y install libboost-all-dev zlib1g-dev  
  
RUN apt-get -y install wget vim supervisor git  
  
RUN apt-get -y install gcc python-dev python-setuptools libffi-dev  
  
RUN apt-get -y install build-essential libtool  
  
RUN easy_install -U pip  
  
RUN wget --no-check-certificate
https://github.com/mwhitaker/docker/releases/download/7.7/vw -P /usr/local/bin  
  
RUN wget --no-check-certificate
https://github.com/mwhitaker/docker/releases/download/7.7/vw-varinfo -P
/usr/local/bin  
  
RUN wget --no-check-certificate
https://github.com/mwhitaker/docker/releases/download/7.7/vw-top-errors -P
/usr/local/bin  
  
RUN wget --no-check-certificate
https://github.com/mwhitaker/docker/releases/download/7.7/perf -P
/usr/local/bin  
  
RUN git clone https://github.com/mwhitaker/phraug2.git  
  
RUN chmod a+x /usr/local/bin/vw  
  
RUN chmod a+x /usr/local/bin/vw-varinfo  
  
RUN chmod a+x /usr/local/bin/vw-top-errors  
  
RUN chmod a+x /usr/local/bin/perf  
  
  
  
###########################################################  
# Here is how to build and run this  
# docker build -t vwdaemon .  
# docker run -it -d -p 26542:26542 vwdaemon  
#  
# Make note of container id and attach to it  
# docker attach 16b6041d0c2f  
# vw -i model.vw -t --daemon --quiet --port 26542  
#  
# is vw daemon running?  
# pgrep vw| wc -l  
#  
# Get out of container but leave it running  
# Ctrl-p Ctrl-q  
#  
#  
# on client>>> echo "| x y z" | nc <ip-address> 26542  
#  
############################################################

