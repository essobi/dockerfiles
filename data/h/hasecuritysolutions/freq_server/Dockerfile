FROM centos:latest  
  
MAINTAINER Justin Henderson justin@hasecuritysolutions.com  
  
RUN yum install -y python git  
RUN cd /opt && git clone https://github.com/SMAPPER/freq_server  
RUN mkdir /var/log/freq_server  
RUN ln -sf /dev/stderr /var/log/freq_server/freq_server.log  
RUN useradd -ms /bin/bash freq_server  
RUN chown -R freq_server: /opt/freq_server  
RUN echo hi  
USER freq_server  
  
EXPOSE 10004  
STOPSIGNAL SIGTERM  
  
CMD /usr/bin/python /opt/freq_server/freq/freq_server.py -ip 0.0.0.0 10004
/opt/freq_server/freq/freq_table.freq  

