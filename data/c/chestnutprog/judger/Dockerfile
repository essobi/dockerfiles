FROM codenvy/ubuntu_jre  
  
RUN sudo apt-get update && \  
sudo apt-get install g++ gcc make gdb gdbserver vim python-pip fp-compiler
python-dev -y && \  
sudo pip install celery  
  
WORKDIR /projects  
RUN sudo touch /usr/local/bin/ssh_key.sh && \  
sudo touch /usr/local/bin/tailsh.sh && \  
sudo chmod 777 /usr/local/bin/ssh_key.sh /usr/local/bin/tailsh.sh && \  
echo "while true\ndo\nif [! -d \"/projects/known_hosts\"];then\nsleep
1\nelse\nmkdir /home/user/.ssh && cp /projects/id_rsa /projects/id_rsa.pub
/projects/known_hosts /home/user/.ssh && cd /projects && sudo cp celeryd
/etc/init.d/celeryd && sudo cp celeryd /etc/init.d/cerelyd && sudo cp
celery.conf /etc/default/celeryd && sudo cp cerely.conf /etc/default/cerelyd
&& cd Lo-runner && sudo ./setup.py install && sudo /etc/init.d/celeryd start
&& sudo /etc/init.d/cerelyd start\nbreak\nfi\ndone" >
/usr/local/bin/ssh_key.sh && \  
echo "nohup /usr/local/bin/ssh_key.sh & \n tail -f /dev/null" >
/usr/local/bin/tailsh.sh  
  
CMD /usr/local/bin/tailsh.sh  

