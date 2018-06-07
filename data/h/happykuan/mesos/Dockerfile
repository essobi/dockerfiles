FROM happykuan/centos  
MAINTAINER "zhangzhikuan" <happykuan@yeah.net>  
  
#mesos version  
ENV MESOS_VERSION=1.0.0  
  
#download  
RUN wget http://www-
us.apache.org/dist/mesos/${MESOS_VERSION}/mesos-${MESOS_VERSION}.tar.gz -O
/tmp/mesos-${MESOS_VERSION}.tar.gz \  
&& cd /tmp/ && tar -zxvf mesos-${MESOS_VERSION}.tar.gz  
  
#install  
RUN cd /tmp/mesos-${MESOS_VERSION} && sh configure  
RUN cd /tmp/mesos-${MESOS_VERSION} && make  
RUN cd /tmp/mesos-${MESOS_VERSION} && make install  
  
#python_mesos  
ENV PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages  
  
##########################################################  
  
CMD ["/bin/bash"]  

