FROM prettynatty/ansible  
  
# Add playbooks to the Docker image  
ADD ansible /srv/ansible  
WORKDIR /srv/ansible  
  
# Run Ansible to configure the Docker image  
RUN ansible-playbook site.yml -c local  
  
# Download sbt  
RUN sbt help  

