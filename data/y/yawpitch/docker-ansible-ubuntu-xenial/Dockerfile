FROM ubuntu:xenial  
LABEL maintainer="Michael Morehouse (yawpitch)"  
  
# Install dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common \  
rsyslog systemd systemd-cron sudo make iputils-ping \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Fix rsyslog.conf.  
RUN sed -i 's/^\\($ModLoad imklog\\)/#\1/' /etc/rsyslog.conf  
  
# Install Ansible.  
RUN apt-add-repository -y ppa:ansible/ansible \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ansible \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Install Ansible inventory file.  
COPY hosts /etc/ansible/hosts  
  
# Restore initctl.  
COPY initctl_faker .  
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  
  
# Clean up.  
RUN apt-get clean && apt-get autoclean -y && apt-get autoremove -y  
  
# Set initial cmd  
CMD ["/lib/systemd/systemd"]  

