  
FROM centos:centos7  
  
MAINTAINER Rafael Ferreira da Silva <rafsilva@isi.edu>  
  
RUN yum -y update  
  
RUN groupadd --gid 510 tutorial  
RUN useradd --create-home --password pegasus123 --uid 510 --gid 510 tutorial  
  
RUN yum -y install nano  
RUN echo "root:pegasus123" | chpasswd  
RUN echo "tutorial:pegasus123" | chpasswd  
  
RUN yum -y install which java-1.7.0-openjdk sudo mysql-devel postgresql-devel
R  
  
# Configure Sudo  
RUN echo -e "tutorial ALL=(ALL) NOPASSWD: /etc/init.d/sshd\n" >> /etc/sudoers  
  
#  
# Configure ulimit  
#  
# Limit max filesize to 4MB  
#  
RUN echo -e "ulimit -f 900000" >> /etc/bashrc  
  
# Get Condor yum repo  
RUN curl -o /etc/yum.repos.d/condor.repo
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo  
RUN yum -y install --nogpgcheck --enablerepo=centosplus condor  
RUN echo -e "TRUST_UID_DOMAIN = True\n" >> /etc/condor/condor_config.local  
RUN echo -e "ALLOW_WRITE = *\n" >> /etc/condor/condor_config.local  
  
RUN usermod -a -G condor tutorial  
RUN chmod -R g+w /var/{lib,log,lock,run}/condor  
  
# Get Pegasus yum repo  
RUN curl -o /etc/yum.repos.d/pegasus.repo
http://download.pegasus.isi.edu/wms/download/rhel/7/pegasus.repo  
RUN yum -y install pegasus  
  
RUN chown -R tutorial /home/tutorial/  
  
# Configure SCP  
RUN yum -y install openssh-server openssh-clients  
RUN perl -pi -e 's/^#RSAAuthentication yes/RSAAuthentication yes/'
/etc/ssh/sshd_config  
RUN perl -pi -e 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/'
/etc/ssh/sshd_config  
RUN perl -pi -e 's/^PasswordAuthentication yes/PasswordAuthentication no/'
/etc/ssh/sshd_config  
RUN perl -pi -e 's/^#UsePAM no/UsePAM no/' /etc/ssh/sshd_config  
RUN perl -pi -e 's/^UsePAM yes/#UsePAM yes/' /etc/ssh/sshd_config  
  
#RUN chmod +r /etc/ssh/sshd_config  
USER tutorial  
  
RUN mkdir /home/tutorial/.ssh  
  
RUN ssh-keygen -t rsa -C tutorial -b 1024 -f /home/tutorial/.ssh/id_rsa -N ''  
RUN cat /home/tutorial/.ssh/id_rsa.pub > /home/tutorial/.ssh/authorized_keys2  
RUN chmod 700 /home/tutorial/.ssh/authorized_keys2  
  
RUN echo -e "condor_master > /dev/null 2>&1" >> /home/tutorial/.bashrc  
RUN echo -e "sudo /etc/init.d/sshd start > /dev/null 2>&1" >>
/home/tutorial/.bashrc  
  
WORKDIR /home/tutorial  

