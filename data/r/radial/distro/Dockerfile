# Dockerfile for the Radial core-distro.  
# Features:  
# - Ubuntu 14.04 LTS  
# - Bash colors  
# - Set locale  
# - Closest apt mirror selection.  
# - Set timezone  
FROM radial/distro-base:en_US  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Select your closest mirror from...  
# US West Coast (N. California): us-west-1.ec2.archive  
# US West Coast (Oregon): us-west-2.ec2.archive  
# US East Coast (N. Virginia): us-east-1.ec2.archive  
# South America (São Paulo, Brazil): sa-east-1.ec2.archive  
# Western Europe (Dublin, Ireland): eu-west-1.ec2.archive  
# NorthEast Asia (Tokyo): ap-northeast-1.ec2.archive  
# SouthEast Asia (Singapore): ap-southeast-1.ec2.archive  
# Australia (Sydney): ap-southeast-2.ec2.archive  
# ... and assign UBUNTU_MIRROR below with your selection  
ENV UBUNTU_MIRROR ap-southeast-2.ec2.archive  
RUN sed "s@archive@$UBUNTU_MIRROR@" -i /etc/apt/sources.list  
  
# Set timezone  
# The city selections might seem arbitrary, but they incorporate daylight
savings  
# time automatically based on time zone and are better then manually picking  
# using the 'Etc/GMT+0' files.  
ENV DEBIAN_FRONTEND noninteractive  
ENV TIMEZONE Australia/Sydney  
RUN echo $TIMEZONE > /etc/timezone &&\  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime &&\  
dpkg-reconfigure tzdata  
  
CMD ["/bin/bash"]  

