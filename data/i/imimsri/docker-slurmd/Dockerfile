FROM imimsri/docker-slurmbase:xenial-v16.05.11  
MAINTAINER SRI IMIM <sri@imim.cat>  
  
RUN mkdir -p /usr/local/etc/slurm  
  
ADD scripts/start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
ADD etc/supervisord.d/slurmd.conf /etc/supervisor/conf.d/slurmd.conf  
  
COPY etc/* etc/  
COPY bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/slurmd-manage  
  
#CMD ["/bin/bash","/root/start.sh"]  
CMD containerpilot -config file:///etc/containerpilot.json
/usr/local/sbin/slurmd -D -v  

