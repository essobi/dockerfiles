FROM centos:latest  
  
MAINTAINER Justin Henderson justin@hasecuritysolutions.com  
  
RUN yum install -y python git curl  
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
RUN python get-pip.py  
RUN cd /opt && git clone https://github.com/MarkBaggett/domain_stats.git  
RUN pip install python-whois  
RUN mkdir /var/log/domain_stats  
RUN ln -sf /dev/stderr /var/log/domain_stats/domain_stats.log  
RUN useradd -ms /bin/bash domain_stats  
RUN chown -R domain_stats: /opt/domain_stats  
USER domain_stats  
  
EXPOSE 20000  
STOPSIGNAL SIGTERM  
  
CMD /usr/bin/python /opt/domain_stats/domain_stats.py -ip 0.0.0.0 20000 -a
/opt/domain_stats/top-1m.csv --preload 0  

