FROM mikefaille/centos-ansible  
# local/centos-ansible  
# Set the environment up  
ENV TERM xterm-256color  
  
RUN ansible all -i "localhost," -c local -m package -a 'name=supervisor
use=yum' && easy_install supervisor-stdout  
  
ADD ansible /ansible-script  
  
# COPY ressources/ansible.ini /etc/supervisord.d/ansible.ini  
ENV MYSQL_HOST=localhost  
ENV MYSQL_USER=root  
  
RUN echo "localhost ansible_connection=local" > /etc/ansible/hosts  
# git clone -b stable-2.1 --depth=1 https://github.com/ansible/ansible-
modules-extras.git /ansible-script/ansible-modules-extras  
# RUN export ANSIBLE_LIBRARY=$ANSIBLE_LIBRARY:/ansible-script/ansible-modules-
extras && \  
# RUN ansible-galaxy install geerlingguy.php  
# TODO erase me  
# RUN ansible localhost -s -m debug -a msg="{{ phabricator_conf.categories.key
}}" -e @/ansible-script/group_vars/all -vv  
RUN ansible-playbook -e phase=building --become-method=su /ansible-
script/main.yml -vv  
  
CMD ["/bin/sh", "-c", "/usr/bin/supervisord -n"]  
# CMD ansible-playbook -e phase=running --become-method=su /ansible-
script/site.yml -vv  
# cd /usr/src && \  
# git clone --depth=1 --branch v2.0.2.0-1 git://github.com/ansible/ansible.git
--recursive && \  
# cd ansible && \  
# make rpm && \  
# yum install -y rpm-
build/ansible-2.0.2.0-0.git201604192124.24d9e5e.HEAD.el7.centos.noarch.rpm &&
\  
# cd .. && rm -R ansible && yum remove -y asciidoc rpm-build python2-devel a2x
make && \  

