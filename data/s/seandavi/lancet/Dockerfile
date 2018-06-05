############################################################  
# Dockerfile to build lofreq variant caller container  
# Based on Ubuntu  
#  
# lancet is on the path  
#  
# usage:  
# docker run seandavi/lancet lancet ....  
#  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Sean Davis <seandavi@gmail.com>  
  
# Update the repository sources list  
RUN apt-get update --fix-missing  
RUN apt-get install -y wget python bzip2 git make  
RUN apt-get install -y sysstat g++ gcc zlib1g-dev zlib1g  
RUN apt-get install -y cmake  
  
RUN echo 'ENABLED="true"' > /etc/default/sysstat  
RUN echo "PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin" >
/etc/cron.d/sysstat  
RUN echo "* * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1
1\n" >> /etc/cron.d/sysstat  
  
  
COPY log_sar /tmp/log_sar  
RUN chmod +x /tmp/log_sar  
  
RUN mkdir -p /opt/  
WORKDIR /opt/  
  
RUN git clone git://github.com/nygenome/lancet.git  
WORKDIR /opt/lancet  
  
RUN make  
  
RUN ln -s /opt/lancet/lancet /usr/bin/lancet  

