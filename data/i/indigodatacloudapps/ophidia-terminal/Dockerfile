# docker build -t ophidia-terminal .  
FROM indigodatacloud/centos-sshd:7  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
  
RUN ansible-galaxy install indigo-dc.ophidia-terminal && \  
ansible-playbook /etc/ansible/roles/indigo-dc.ophidia-terminal/tests/ophidia-
terminal.yml  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

