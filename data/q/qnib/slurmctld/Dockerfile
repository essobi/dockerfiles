###### QNIBTerminal images  
FROM qnib/slurm  
  
ADD etc/supervisord.d/slurmctld.ini /etc/supervisord.d/  
ADD etc/consul.d/check_slurmctld.json /etc/consul.d/  
ADD opt/qnib/slurm/bin/ /opt/qnib/slurm/bin/  
  
# Slurmstats  
ADD etc/supervisord.d/slurmstats.ini /etc/supervisord.d/  
ADD opt/qnib/slurm/bin/slurmstats.py /opt/qnib/slurm/bin/  
# Scratch setup  
ADD etc/supervisord.d/scratchsetup.ini /etc/supervisord.d/  
ADD opt/qnib/bin/scratchsetup.sh /opt/qnib/bin/  
RUN yum install -y freetype-devel libpng-devel gcc gcc-c++ graphviz-devel && \  
pip install clustershell networkx matplotlib pygraphviz  
ADD etc/sensu/conf.d/slurmctld.json /etc/sensu/conf.d/  
ADD opt/qnib/slurm/bin/check_slurmctld.sh /opt/qnib/slurm/bin/  

