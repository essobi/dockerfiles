FROM ubuntu:trusty  
MAINTAINER developers@khipu.com  
  
RUN echo 'America/Santiago' > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN dpkg-reconfigure --frontend noninteractive locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
CMD ["/bin/true"]  

