FROM fedora  
  
RUN mkdir /var/run/sshd  
  
RUN dnf -y upgrade && \  
dnf -y install git gcc python python3 python-pip python-gevent python-dateutil
nano emacs-nox vim \  
openssh-server procps-ng && \  
pip install --upgrade pip && \  
pip install pyyaml pytz requests grequests python-dateutil && \  
dnf -y clean all  
  
# This lets us exit sshd cleanly  
COPY dumb-init_1.2.1_amd64 /usr/bin/dumb-init  
RUN chmod +x /usr/bin/dumb-init  
  
# Create root's ssh config directory  
RUN mkdir -p /root/.ssh && \  
touch /root/.ssh/authorized_keys && \  
chmod 644 /root/.ssh/authorized_keys  
  
COPY sshd_config /etc/ssh/sshd_config  
  
RUN mkdir /autograder  
COPY update_harness.py /autograder/update_harness.py  
COPY update_and_run_harness.sh /autograder/update_and_run_harness.sh  
COPY harness.py /autograder/harness.py  
  
COPY start_sshd.sh /usr/local/sbin/start_sshd.sh  
COPY ssh_wrapper.sh /usr/local/sbin/ssh_wrapper.sh  
  
COPY motd /etc/motd  
  
# Set the locale to UTF-8 to ensure that Unicode output is encoded correctly  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
CMD ["/autograder/update_and_run_harness.sh"]  

