FROM andypohl/htcondor  
  
MAINTAINER Andy Pohl <apohl@morgridge.org>  
  
# Pick a username.  
ENV USER htandy  
  
USER root  
  
RUN yum -y install \  
jyum \  
java-1.7.0-openjdk-devel \  
mysql-devel \  
postgresql-devel \  
git \  
openssl \  
openssh-server \  
openssh-clients && \  
curl -o /etc/yum.repos.d/pegasus.repo
http://download.pegasus.isi.edu/wms/download/rhel/7/pegasus.repo && \  
yum -y install pegasus && \  
perl -pi -e 's/^#RSAAuthentication yes/RSAAuthentication yes/'
/etc/ssh/sshd_config && \  
perl -pi -e 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/'
/etc/ssh/sshd_config && \  
perl -pi -e 's/^PasswordAuthentication yes/PasswordAuthentication no/'
/etc/ssh/sshd_config && \  
perl -pi -e 's/^#UsePAM no/UsePAM no/' /etc/ssh/sshd_config && \  
perl -pi -e 's/^UsePAM yes/#UsePAM yes/' /etc/ssh/sshd_config && \  
# related to pegasus dashboard (pegasus-service) (DOESN'T WORK YET)  
mkdir -p /var/log/pegasus && \  
chgrp -R condor /var/log/pegasus && \  
chmod -R g+w /var/log/pegasus && \  
yum clean all  
  
USER ${USER}  
  
RUN mkdir /home/${USER}/.ssh && chmod 700 /home/${USER}/.ssh && \  
ssh-keygen -t rsa -C ${USER} -b 1024 -f /home/${USER}/.ssh/id_rsa -N '' && \  
cat /home/${USER}/.ssh/id_rsa.pub > /home/${USER}/.ssh/authorized_keys2 && \  
chmod 700 /home/${USER}/.ssh/authorized_keys2 && \  
mkdir /home/${USER}/bin && \  
echo -e "export PATH=\${PATH}:/home/${USER}/bin" >> /home/${USER}/.bashrc && \  
echo -e "sudo pegasus-service --host \$(hostname) --port 5000 >>
/var/log/pegasus/pegasus.log 2>> /var/log/pegasus/pegasus.log &" >>
/home/${USER}/.bashrc && \  
echo -e "sudo /etc/init.d/sshd start > /dev/null 2>&1" >>
/home/${USER}/.bashrc  
  
COPY fix_daxgen_py.sh /home/${USER}/bin  
  
EXPOSE 5000  
  
CMD [ "/bin/bash" ]  

