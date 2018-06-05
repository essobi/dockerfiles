# following steps from https://slurm.schedmd.com/quickstart_admin.html  
FROM nlesc/xenon-slurm-ssh  
  
# become root user  
USER root  
  
# add the generic script to compile and install slurm  
ADD install_slurm.sh /usr/local  
  
# slurm wants munged including its development files  
RUN apt-get update && apt-get install -y munge libmunge2  
  
# A munge authentication key should have been generated at
/etc/munge/munge.key  
# during installation of munge. If not, you can create one with the create-
munge-key program or  
# by following one of the steps outlined at
https://github.com/dun/munge/blob/master/QUICKSTART  
# Apply the recommended permissions from
https://github.com/dun/munge/wiki/Installation-Guide#securing-the-
installation;  
# create /var/run/munge because that doesn't get created during install for
some reason.  
RUN chmod 0700 /etc/munge && \  
chmod 0711 /var/lib/munge && \  
chmod 0700 /var/log/munge && \  
mkdir /var/run/munge && \  
chmod 0755 /var/run/munge && \  
chmod 0400 /etc/munge/munge.key  
  
# change ownership of all munge related directories to user 'munge'  
RUN chown -R munge:munge /etc/munge /var/lib/munge /var/log/munge
/var/run/munge  
  
# make a slurm user  
RUN groupadd --system slurm && useradd --system --gid slurm --create-home
slurm  
  
# change user slurm's password to 'slurm'  
RUN echo slurm:slurm | chpasswd  
  
# make directory structure required by Slurm nodes  
RUN mkdir -p /var/spool/slurmctld/state  
RUN chown -R slurm:slurm /var/spool/slurmctld  
  
# make slurm sysconfig directory  
RUN mkdir -p /usr/local/etc/slurm  
  
# make slurm logging directory  
RUN mkdir -p /var/log/slurm  
RUN chown -R slurm:slurm /var/log/slurm  
  
# ADD slurm.cert from context to sysconfig directory  
ADD slurm.cert /usr/local/etc/slurm/slurm.cert  
  
# ADD slurm.key from context to sysconfig directory  
ADD slurm.key /usr/local/etc/slurm/slurm.key  
  
# set permissions on key file  
RUN chmod 600 /usr/local/etc/slurm/slurm.key  
  
# change ownership to the slurm user  
RUN chown slurm:slurm /usr/local/etc/slurm/slurm.key  
  
# set workdirectory to something sane  
WORKDIR /home/xenon/  
  
# add a test job script  
ADD test-slurm.job /home/xenon/test-slurm.job  
RUN chown xenon:xenon /home/xenon/test-slurm.job  
  
ADD start-services.sh /etc/start-services.sh  
RUN chmod +x /etc/start-services.sh  
CMD /etc/start-services.sh  
  

