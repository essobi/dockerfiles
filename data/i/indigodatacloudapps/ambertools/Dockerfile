# docker build --rm -t ambertools .  
FROM indigodatacloud/ubuntu-sshd:16.04  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Container image to run AmberTools v17"  
  
ENV AMBERHOME /usr/local/amber16  
ENV PATH $PATH:$AMBERHOME/bin  
ENV LD_LIBRARY_PATH $AMBERHOME/lib  
RUN ansible-galaxy install git+https://github.com/indigo-dc/ansible-role-
ambertools.git && \  
ansible-playbook /etc/ansible/roles/ansible-role-
ambertools/tests/ambertools.yml  
  
EXPOSE 22  
CMD /etc/init.d/vmcontext start; /usr/sbin/sshd -D  

