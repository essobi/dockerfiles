FROM ubuntu:16.04  
MAINTAINER Ernestas Poskus <hierco@gmail.com>  
  
# Install dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-software-properties \  
software-properties-common \  
rsyslog systemd systemd-cron sudo \  
iproute \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
RUN sed -i 's/^\\($ModLoad imklog\\)/#\1/' /etc/rsyslog.conf  
#ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf  
RUN add-apt-repository -y ppa:ansible/ansible \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ansible \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Install/prepare Ansible  
RUN mkdir -p /etc/ansible/  
RUN mkdir -p /opt/ansible/roles  
RUN rm -f /opt/ansible/hosts  
RUN printf '[local]\nlocalhost ansible_connection=local\n' >
/etc/ansible/hosts  

