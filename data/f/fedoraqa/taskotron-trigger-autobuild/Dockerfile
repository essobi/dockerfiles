FROM fedora:24  
RUN dnf install -y fedmsg fedmsg-hub git koji python2-requests python2-twisted
PyYAML python2-mongoquery && dnf clean all &&\  
mkdir -p /etc/taskotron /var/log/taskotron-trigger /var/lib/taskotron-trigger  
  
COPY ./conf/trigger.cfg.example /etc/taskotron/trigger.cfg  
COPY ./conf/trigger_rules.yml.example /etc/taskotron/trigger_rules.yml  
COPY ./docker_data/critpath_whitelist.example /var/lib/taskotron-
trigger/critpath_whitelist  
COPY ./fedmsg.d/taskotron-trigger.py /etc/fedmsg.d/  
COPY . /usr/src/taskotron-trigger  
  
WORKDIR /usr/src/taskotron-trigger  
RUN python setup.py build && python setup.py install -O1 --skip-build --root /  
  
CMD ["/usr/bin/fedmsg-hub"]  

