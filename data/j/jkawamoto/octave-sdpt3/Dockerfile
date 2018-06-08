#  
# Octave with SDPT3.  
#  
# Usage:  
# - mount your scripts in /data.  
#  
FROM ubuntu:latest  
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>  
  
# Install packages.  
ENV TERM vt100  
RUN apt-get update && \  
apt-get install -y git octave liboctave-dev && \  
apt-get upgrade -y && apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/  
  
# Download sdpt3  
WORKDIR /root  
RUN git clone https://github.com/sqlp/sdpt3.git  
ADD .octaverc .  
  
WORKDIR /data  
CMD ["octave"]  

