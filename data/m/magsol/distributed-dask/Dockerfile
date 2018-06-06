FROM ubuntu:14.04.4  
MAINTAINER Shannon Quinn "spq@uga.edu"  
USER root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Some basic updates.  
RUN apt-get -y update  
RUN apt-get install -y wget rsync build-essential openjdk-7-jdk vim emacs git  
  
# Install Anaconda and set up the basic Python environment.  
RUN git clone https://gist.github.com/165330b48c869a7ccc33.git scripts && \  
scripts/conda3-distributed.sh && rm -rf scripts/  
  
# A few useful config options.  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
ENV PATH /opt/python/bin:$PATH  
  
# Move the startup scripts over.  
COPY start-scheduler.sh /tmp  
COPY start-worker.sh /tmp  
RUN chmod +x /tmp/*.sh && mv /tmp/*.sh /bin/  

