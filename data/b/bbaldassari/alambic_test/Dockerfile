  
FROM centos:7  
MAINTAINER Boris boris.baldassari@castalia.solutions  
  
EXPOSE 3000  
# Install  
RUN yum -y update; yum clean all  
  
# Install openssh  
RUN yum -y install openssh-server passwd; yum clean all  
RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
# Install needed applications  
RUN yum install -y passwd perl-CPAN gcc make bzip2 git libxml2-devel openssl
openssl-devel; yum clean all  
  
# Install postgresql 9.5 client  
RUN rpm -Uvh
https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-
centos95-9.5-3.noarch.rpm \  
&& yum install -y postgresql95 postgresql95-devel  
  
# Create user alambic, password passpass  
RUN adduser alambic && \  
echo passpass | passwd alambic --stdin  
  
# Run initialisation script to install perlbrew and all mojo stuff  
COPY 00_install_deps.sh /root/00_install_deps.sh  
RUN chmod +x /root/00_install_deps.sh  
RUN sh /root/00_install_deps.sh  
  
USER alambic  
RUN git clone https://bitbucket.org/BorisBaldassari/alambic.git
/home/alambic/alambic  
COPY alambic_start.sh /home/alambic/alambic_start.sh  
COPY alambic_test.sh /home/alambic/alambic_test.sh  
COPY alambic.conf /home/alambic/alambic/mojo/alambic.conf  
  
USER root  
COPY alambic_start_wrapper.sh /root/alambic_start_wrapper.sh  
COPY alambic_test_wrapper.sh /root/alambic_test_wrapper.sh  
RUN chmod +x /home/alambic/alambic_start.sh  
RUN chmod +x /home/alambic/alambic_test.sh  
RUN chmod +x /root/alambic_start_wrapper.sh  
RUN chmod +x /root/alambic_test_wrapper.sh  
  
# Install R and all dependencies  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm; \  
yum install -y R;  
RUN yum install -y wget libcurl-devel  
  
COPY alambic_install_r.R /home/alambic/  
RUN Rscript /home/alambic/alambic_install_r.R  
  
CMD ["/usr/sbin/sshd", "-D"]  
  

