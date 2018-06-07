FROM lewisw/docker-test-runner  
MAINTAINER Lewis Wright <lewis@allwrightythen.com>  
  
# Create the structure  
WORKDIR /project  
  
RUN mkdir -p app/config && echo "parameters: []" >
app/config/parameters.yml.dist  
  
# Copy the role requirements and run them  
COPY install-dependencies.sh ansible/install-dependencies.sh  
COPY requirements.yml ansible/requirements.yml  
RUN /ansible_dependencies  
  
# Copy any files used in provisioning & provision  
COPY . ansible/  
RUN /apt_cacher leeroy.vivait.co.uk; \  
ansible-playbook ansible/setup.yml -i ansible/inventories/build \  
-e "mysql_databases=[] mysql_users=[] apache_vhosts=[] override_parameters=[] parameters=[] apache_create_vhosts=false" && \  
/graceful_shutdown  

