FROM centos  
  
MAINTAINER Tinsjourney <tintin@gnali.org>  
  
RUN yum -y --setopt="tsflags=nodocs" update && \  
yum -y --setopt="tsflags=nodocs" install \  
PyYAML \  
python-jinja2 \  
yum clean all && \  
rm -rf /var/cache/yum/*  
  
ADD http://releases.ansible.com/ansible/ansible-2.2.1.0.tar.gz /opt/ansible/  
RUN tar -xzf /opt/ansible/ansible-2.2.1.0.tar.gz --strip-components=1 -C
/opt/ansible  
  
RUN useradd -u 1000 ansible  
USER ansible  
ENV PATH
/opt/ansible/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV PYTHONPATH /opt/ansible/lib:  
ENV MANPATH /opt/ansible/docs/man:  
RUN echo "localhost ansible_connection=local" > ~/ansible_hosts  
ENV ANSIBLE_INVENTORY=~/ansible_hosts  
WORKDIR /home/ansible  
ENTRYPOINT ["/opt/ansible/bin/ansible"]  

