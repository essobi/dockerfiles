FROM fedora:20  
MAINTAINER Maxim Kolchin <kolchinmax@gmail.com>  
  
WORKDIR /root  
  
RUN yum install libffi-devel python-pip python-devel gcc openssl-devel -y  
RUN yum upgrade -y  
RUN yum clean all  
  
RUN pip install --upgrade twisted  
RUN pip install ez_setup six pyopenssl pycrypto wsaccel ujson  
RUN pip install --upgrade distribute  
  
RUN pip install crossbar[tls,msgpack,manhole,system]  
  
RUN crossbar version  
  
RUN mkdir crossbar  
WORKDIR crossbar  
RUN crossbar init  
  
ADD config.json /root/crossbar/.crossbar/  
  
EXPOSE 80  
CMD crossbar start --cbdir /root/crossbar/.crossbar  

