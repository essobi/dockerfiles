FROM centos:centos7  
  
MAINTAINER Rajiv Mayani <mayani@isi.edu>  
  
RUN yum -y update  
  
RUN useradd --create-home --password pegasus123 tutorial  
  
RUN yum -y install which jyum install java-1.7.0-openjdk-devel sudo mysql-
devel postgresql-devel wget git  
  
# Configure Sudo  
RUN echo -e "tutorial ALL=(ALL) NOPASSWD: /etc/init.d/sshd\n" >> /etc/sudoers  
  
#  
# Configure ulimit  
#  
# NOOOO ----> Limit max filesize to 4MB  
#  
#RUN echo -e "ulimit -f 4000" >> /etc/bashrc  
# Get Condor yum repo  
#RUN curl -o /etc/yum.repos.d/condor.repo
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo  
#RUN yum -y install --enablerepo=centosplus condor  
#RUN echo -e "TRUST_UID_DOMAIN = True\n" >> /etc/condor/condor_config.local  
#RUN echo -e "ALLOW_WRITE = *\n" >> /etc/condor/condor_config.local  
#RUN usermod -a -G condor tutorial  
#RUN chmod -R g+w /var/{lib,log,lock,run}/condor  
# Get Condor yum repo  
#RUN mkdir /run/lock  
RUN curl -o /etc/yum.repos.d/condor.repo
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo  
RUN yum -y install --enablerepo=centosplus condor  
RUN echo -e "TRUST_UID_DOMAIN = True\n" >> /etc/condor/condor_config.local  
RUN echo -e "ALLOW_WRITE = *\n" >> /etc/condor/condor_config.local  
RUN usermod -a -G condor tutorial  
RUN chmod -R g+w /var/{lib,log,lock,run}/condor  
  
# Get Pegasus yum repo  
RUN curl -o /etc/yum.repos.d/pegasus.repo
http://download.pegasus.isi.edu/wms/download/rhel/7/pegasus.repo  
RUN yum -y install pegasus  
#RUN yum -y install graphviz  
#RUN rpm -ivh
http://download.pegasus.isi.edu/pegasus/4.5.0/pegasus-4.5.0-1.el7.x86_64.rpm  
#RUN cp -rf /usr/share/doc/pegasus/tutorial/* /home/tutorial/  
#RUN chmod +x /home/tutorial/{generate_dax.py,plan_dax.sh}
/home/tutorial/bin/*  
#ADD pegasus/doc/tutorial /home/tutorial/  
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
  
RUN git clone https://github.com/dispel4py/pegasus_dispel4py.git  
RUN git clone https://github.com/dispel4py/dispel4py.git  
  
USER root  
  
RUN yum install -y python-setuptools  
RUN yum install -y zip  
RUN yum install -y unzip  
RUN yum install -y vim  
RUN easy_install pip  
RUN pip install requests  
RUN cd dispel4py && python setup.py install  
RUN chmod u+x /home/tutorial/pegasus_dispel4py/simple_experiment/command-job*  
RUN chmod u+x /home/tutorial/pegasus_dispel4py/storm_experiment/command-job.sh  
RUN chmod u+x /home/tutorial/pegasus_dispel4py/tc_cross_correlation/*  
RUN chmod u+x
/home/tutorial/pegasus_dispel4py/cross_correlation_experiment/command-job*  
  
######## Storm stuff  
#RUN scl enable python27 "pip install thrift"  
RUN pip install thrift  
  
USER tutorial  
RUN cd /home/tutorial && \  
wget http://shinyfeather.com/storm/apache-storm-0.10.0/apache-
storm-0.10.0.tar.gz && \  
tar xzf apache-storm-0.10.0.tar.gz && \  
mkdir /home/tutorial/.storm && \  
echo 'nimbus.host: "nimbus"' > /home/tutorial/.storm/storm.yaml  
  
USER root  
RUN cp -r /home/tutorial/pegasus_dispel4py/Docker/storm
/home/tutorial/dispel4py/.  
RUN cp -r /home/tutorial/pegasus_dispel4py/tc_cross_correlation
/home/tutorial/dispel4py/resources/.  
RUN cp -r /home/tutorial/pegasus_dispel4py/tc_cross_correlation
/home/tutorial/dispel4py/.  
RUN cp /home/tutorial/pegasus_dispel4py/Docker/storm.py
/home/tutorial/dispel4py/resources/.  
RUN cp -r /home/tutorial/dispel4py/dispel4py
/home/tutorial/dispel4py/resources/.  
RUN chown tutorial:tutorial -R /home/tutorial/dispel4py/resources  
##### Obspy stuff  
RUN wget
http://dl.fedoraproject.org/pub/epel/7/x86_64/p/python2-future-0.15.2-7.el7.noarch.rpm  
RUN rpm -Uvh python2-future-0.15.2-7.el7.noarch.rpm  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y install numpy python-matplotlib  
RUN yum -y install python-basemap  
RUN yum -y install python-basemap-data-hires.noarch  
RUN cd /etc/yum.repos.d/ && \  
wget
https://copr.fedorainfracloud.org/coprs/qulogic/obspy/repo/epel-7/qulogic-
obspy-epel-7.repo  
RUN yum -y install python-obspy  
  
##### Connect to OpenMPI cluster  
RUN git clone https://github.com/dispel4py/docker.openmpi.git  
RUN chmod -R 600 /home/tutorial/docker.openmpi/ssh/*  
RUN chown -R tutorial:tutorial /home/tutorial/docker.openmpi/ssh  
RUN chown -R tutorial:tutorial /home/tutorial/dispel4py/tc_cross_correlation  

