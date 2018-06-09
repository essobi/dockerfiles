# EXABGP latest  
FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends wget python lv emacs23-nox
python-setuptools busybox-syslogd supervisor  
  
ENV HOME /root  
WORKDIR /root  
  
RUN wget --no-check-certificate https://github.com/Exa-
Networks/exabgp/archive/3.4.10.tar.gz  
RUN tar xzf 3.4.10.tar.gz  
RUN cd exabgp-3.4.10 && python setup.py install  
  
RUN mkdir /usr/local/etc/exabgp  
RUN /usr/local/bin/exabgp --fi > /usr/local/etc/exabgp/exabgp.env  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ENTRYPOINT ["/usr/bin/supervisord"]  

