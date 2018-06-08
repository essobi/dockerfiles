## QNIBTerminal image  
FROM qnib/slurm:cos7  
  
ADD etc/supervisord.d/slurmd.ini /etc/supervisord.d/  
ADD etc/consul.d/slurmd.json /etc/consul.d/  
ADD /opt/qnib/slurm/bin/check_slurmd.sh /opt/qnib/slurm/bin/  

