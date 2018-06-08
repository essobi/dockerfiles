# docker build -t powerfit .  
FROM indigodatacloud/ubuntu-sshd:14.04  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
  
RUN ansible-galaxy install marcoverl.disvis-powerfit && \  
ansible-playbook /etc/ansible/roles/marcoverl.disvis-
powerfit/tests/powerfit75.yml  
  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu:/usr/local/lib64  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

