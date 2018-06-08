###### QNIBng image  
FROM qnib/terminal:cos7  
  
RUN yum install -y bzip2 make gcc munge-libs munge-devel munge lua-devel && \  
curl -fsL http://www.schedmd.com/download/total/slurm-15.08.3.tar.bz2 | tar
xfj - -C /opt/ && \  
cd /opt/slurm-15.08.3/ && \  
./configure && make && make install  
ADD etc/supervisord.d/munged.ini /etc/supervisord.d/  
ADD etc/consul.d/munged.json /etc/consul.d/  
## User slurm  
RUN useradd -u 2001 -d /home/slurm slurm  
  
## install consul-template  
ADD etc/consul-templates/slurm/slurm.conf.tmpl /etc/consul-templates/slurm/  
ADD usr/local/etc/slurm.conf /usr/local/etc/slurm.conf  
ENV LD_LIBRARY_PATH=/usr/local/lib/  
# Setup slurm (soft) restart, if cluster size changes  
ADD opt/qnib/slurm/bin/reread.sh /opt/qnib/slurm/bin/  
ADD etc/supervisord.d/slurm_update.ini /etc/supervisord.d/  
ADD etc/munge/munge.key /etc/munge/  
RUN chmod 600 /etc/munge/munge.key && \  
chown root: /var/log/munge/ /run/munge /var/lib/munge /etc/munge  
ADD opt/qnib/munge/bin/check.sh /opt/qnib/munge/bin/  
ADD etc/sensu/conf.d/munge.json /etc/sensu/conf.d/  

