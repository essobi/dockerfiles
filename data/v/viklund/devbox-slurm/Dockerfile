#
=============================================================================  
# viklund/devbox-slurm  
#
=============================================================================  
FROM viklund/centos-devbox:latest  
MAINTAINER Johan Viklund <johan.viklund@bils.se>  
  
# Munge, httpd and mysql is for slurm  
RUN yum -y install munge munge-devel httpd \  
mysql mysql-devel mysql mysql-server && \  
create-munge-key  
  
WORKDIR /usr/local  
RUN MAKEFLAGS=-j12 \  
# Clone slurm  
git clone https://github.com/SchedMD/slurm.git && \  
cd slurm && \  
git checkout tags/slurm-14-03-9-1 && \  
# Configure and install slurm  
./configure --prefix=/usr --sysconfdir=/etc/sysconfig/slurm --with-
mysql_config=/usr/local/bin && \  
make && \  
make install && \  
mkdir -p /etc/sysconfig/slurm && \  
cp etc/init.d.slurm /etc/init.d/slurmd && \  
chmod +x /etc/init.d/slurmd && \  
cp -rf doc/html /var/www/html/slurm && \  
chown -R apache:apache /var/www/html/slurm  
  
RUN chown -R root:root /var/log/munge && \  
chown -R root:root /var/lib/munge && \  
mkdir /var/run/munge && \  
chown -R root:root /var/run/munge && \  
chown -R root:root /etc/munge  
  
RUN adduser -u 501 slurm && \  
echo 'slurm:slurm' | chpasswd && \  
mkdir /var/log/slurm && \  
touch /var/log/slurm/job_completions && \  
touch /var/log/slurm/accounting && \  
chown -R slurm:slurm /var/log/slurm  
  
RUN touch /var/spool/last_config_lite && \  
touch /var/spool/last_config_lite.new && \  
chown slurm:slurm /var/spool/last_config_lite*  
  
RUN chown root:slurm /var/spool && \  
chmod g+w /var/spool  
  
COPY supervisor_slurm.conf /etc/supervisord/  
COPY slurm.conf /etc/sysconfig/slurm/slurm.conf  
COPY slurm-bootstrap /etc/  
  
RUN chmod +x /etc/slurm-bootstrap  

