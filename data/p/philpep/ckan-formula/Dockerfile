FROM centos:7  
RUN yum -y install epel-release && \  
yum -y install https://repo.saltstack.com/yum/redhat/salt-
repo-2016.11-2.el7.noarch.rpm && \  
yum -y install
https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-
redhat94-9.4-2.noarch.rpm && \  
yum clean expire-cache && \  
yum -y install salt-minion python-pygit2 git net-tools libgit2-devel  
  
ENV LANG en_US.UTF-8  
ENV SHELL /bin/bash  
  
ADD test/minion.conf /etc/salt/minion.d/minion.conf  
ADD test/salt /srv/salt  
ADD test/pillar /srv/pillar  
ADD ckan /srv/formula/ckan  
ADD solr /srv/formula/solr  
ADD _states /srv/formula/_states  
ARG SALT_ARGS=state.highstate  
RUN salt-call -l debug --hard-crash $SALT_ARGS  
  
ARG USER=ckan  
USER $USER  
CMD ["/home/ckan/bin/supervisord", "--nodaemon"]  

