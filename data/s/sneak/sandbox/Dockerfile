FROM ubuntu:16.04  
ADD ./sources.list /etc/apt/sources.list  
  
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d  
ADD ./run.sh /tmp/run.sh  
RUN bash /tmp/run.sh && rm /tmp/run.sh  
ADD ./my_init /usr/sbin/my_init  
RUN chmod +x /usr/sbin/my_init  
CMD /usr/sbin/my_init  

