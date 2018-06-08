FROM centos:centos7  
MAINTAINER Fredrik Brännbacka <fredrik@madcrew.se>  
  
WORKDIR /tmp  
RUN yum install -y gcc python-devel tar sysstat  
# Install Setup Tools and pip  
RUN curl -O
https://pypi.python.org/packages/source/s/setuptools/setuptools-7.0.tar.gz&&tar
-xf setuptools-7.0.tar.gz  
WORKDIR setuptools-7.0  
RUN python2.7 setup.py install  
RUN curl https://bootstrap.pypa.io/get-pip.py | python2.7 -  
RUN pip install psutil  
ADD collect_metrics.py /usr/bin/collect_metrics  
RUN chmod +x /usr/bin/collect_metrics  
  
ENV DB_HOST localhost  
ENV DB_PORT 2003  
ENV DB_NAME metrics  
ENV DB_USER root  
ENV DB_PASS root  
ENV COLLECT_INTERVAL 10  
ENV METRICS_SERIES metrics  
WORKDIR /  
CMD ["/usr/bin/collect_metrics"]  

