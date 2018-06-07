FROM centos:centos6  
  
# Install all necessary binaries  
RUN yum install -y tar which openssh-server openssh-
clients-5.3p1-94.el6.x86_64 sudo  
  
# Copy installation files  
ADD dmxtar* /tmp/  
RUN cat `ls /tmp/dmxtar* | sort` > /tmp/dmexpress.tar.gz  
RUN (cd /usr ; tar zxf /tmp/dmexpress.tar.gz)  
RUN rm -v /tmp/dmxtar* /tmp/dmexpress.tar.gz  
  
# Copy local pam.d/sshd (Needed for ssh login)  
ADD ss_sshd /etc/pam.d/sshd  
  
# Unpacking required ssh configuration  
RUN echo $'\nBanner /etc/ssh/sshd_banner\n' >> /etc/ssh/sshd_config  
ADD sshd_banner /etc/ssh/  
  
# Set environment  
ENV PATH $PATH:/usr/dmexpress/bin  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/dmexpress/lib  
  
# Create user  
RUN useradd -m -d /home/syncsort/ -s /bin/bash -p $(echo syncsort | openssl
passwd -1 -stdin) syncsort  
  
# Make syncsort a sudoer  
RUN echo $'syncsort ALL=(ALL) ALL\n' > /etc/sudoers.d/syncsort_user  
  
RUN chown -R syncsort /usr/dmexpress  
  
# Add startup script  
ADD ss_bashrc /home/syncsort/.bashrc  
ADD ss_initial_startup.sh /home/syncsort/ss_initial_startup.sh  
  
# Move DMX UCAs to Docker  
ADD UseCaseAccelerators.tar.gz /usr/dmexpress/examples/  
RUN chown -R syncsort:syncsort /usr/dmexpress/examples/UseCaseAccelerators/  
RUN chmod -R a+r /usr/dmexpress/examples/  
RUN find /usr/dmexpress/examples/ -type d -exec chmod a+x {} \;  
  
# Expose dmxd port  
EXPOSE 32636  
# Expose sshd port  
EXPOSE 22  
# Copy daemon start script  
ADD startd.sh /tmp/  
RUN chmod +x /tmp/startd.sh  
  
CMD /tmp/startd.sh  

