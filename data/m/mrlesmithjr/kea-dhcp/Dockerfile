FROM mrlesmithjr/ubuntu-ansible:16.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME [ "/etc/kea","/var/lib/kea","/var/log/kea" ]  
  
CMD ["kea-dhcp4", "-c", "/etc/kea/kea-dhcp4.conf"]  
  
EXPOSE 67/udp 68/udp  

