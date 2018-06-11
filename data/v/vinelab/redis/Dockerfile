FROM vinelab/base  
  
MAINTAINER Abed Halawi <abed.halawi@vinelab.com>  
  
# Install dependencies  
RUN yum install -y gcc gcc-c++ make  
  
# Go to /tmp and perform the installation from there  
WORKDIR /tmp  
  
# Download and uncompress source  
RUN wget http://download.redis.io/redis-stable.tar.gz  
RUN tar xzf redis-stable.tar.gz  
  
WORKDIR redis-stable  
  
RUN make && make install  
  
# Move compiled binaries  
RUN cp -f src/* /usr/local/bin/  
  
# Configure  
RUN mkdir -p /etc/redis  
RUN cp -f *.conf /etc/redis  
  
WORKDIR /  
  
ADD redis.ini /etc/supervisord.d/redis.ini  
  
RUN echo 'vm.swappiness=0' >> /etc/sysctl.conf  
RUN echo 'vm.overcommit_memory=1' >> /etc/sysctl.conf  
RUN echo 'fs.file-max = 500000' >> /etc/sysctl.conf  
RUN echo '* soft nofile 60000' >> /etc/security/limits.conf  
RUN echo '* hard nofile 60000' >> /etc/security/limits.conf  
  
# Make it not save at all  
RUN sed -i '/^save.*$/d' /etc/redis/redis.conf  
  
ADD launch.sh /launch.sh  
RUN chmod +x /launch.sh  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Expose ports  
EXPOSE 6379  
CMD ["/bin/bash", "-c", "/launch.sh"]  
  
# Clean up  
RUN rm -rf /tmp/*  
RUN yum remove -y gcc gcc-c++  
RUN yum clean all  

