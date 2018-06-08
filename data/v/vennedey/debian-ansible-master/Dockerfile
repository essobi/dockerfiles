FROM debian:jessie  
MAINTAINER Falco Vennedey "docker@vennedey.net"  
ENV PRIVATEKEY ""  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y ssh vim less man python git ca-certificates python-setuptools gcc
libpython-all-dev libyaml-dev libffi-dev libssl-dev  
  
RUN cd /root && git clone git://github.com/ansible/ansible.git --recursive  
RUN easy_install pip  
RUN pip install paramiko PyYAML Jinja2 httplib2 six pycrypto  
RUN echo "source /root/ansible/hacking/env-setup" >> /root/.bashrc  
RUN cp /root/ansible/examples/ansible.cfg /root/.ansible.cfg  
  
COPY files/usr/local/sbin/init.sh /usr/local/sbin/init.sh  
RUN chmod 700 /usr/local/sbin/init.sh  
  
RUN mkdir /root/.ssh && touch /root/.ssh/id_rsa && chmod 400 /root/.ssh/id_rsa  
CMD /usr/local/sbin/init.sh  

