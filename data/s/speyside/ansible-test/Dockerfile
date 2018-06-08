FROM ubuntu:12.04  
ARG TEST_USER  
ENV TEST_USER ${TEST_USER:-ubuntu}  
  
# Configure Ansible requirements  
RUN apt-get update && \  
apt-get install -y python ssh sudo && \  
mkdir /var/run/sshd  
  
# Configure the test user  
RUN useradd -s /bin/bash $TEST_USER && \  
bash -c 'echo -e "${TEST_USER}\n${TEST_USER}" | passwd $TEST_USER' && \  
echo "${TEST_USER} ALL=NOPASSWD: ALL" >> /etc/sudoers && \  
mkdir -p /home/$TEST_USER/.ssh  
  
# Copy test ssh key  
COPY id_rsa /home/$TEST_USER/.ssh  
COPY id_rsa.pub /home/$TEST_USER/.ssh  
  
# Update ssh permissions  
RUN cat /home/$TEST_USER/.ssh/id_rsa.pub >>
/home/$TEST_USER/.ssh/authorized_keys && \  
chmod 700 /home/$TEST_USER/.ssh && \  
chmod 600 /home/$TEST_USER/.ssh/id_rsa && \  
chmod 644 /home/$TEST_USER/.ssh/id_rsa.pub && \  
chmod 600 /home/$TEST_USER/.ssh/authorized_keys && \  
chown -R $TEST_USER:$TEST_USER /home/$TEST_USER/  
  
EXPOSE 22  
CMD cat /home/$TEST_USER/.ssh/id_rsa && /usr/sbin/sshd -D  

