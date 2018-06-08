FROM petkr/torque-base  
  
COPY torque.setup /torque.setup  
COPY entrypoint.sh /  
  
RUN yum -y install openssh-server && \  
yum clean all && \  
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \  
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N '' && \  
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''  
  
RUN mkdir -p /var/spool/torque/checkpoint/ && \  
mkdir -p /var/spool/torque/server_priv && \  
chmod +x torque.setup && \  
chmod +x entrypoint.sh && \  
useradd testuser -u 9999 && \  
echo "testuser" | passwd "testuser" \--stdin  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]

