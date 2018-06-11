FROM ansible/ubuntu14.04-ansible  
MAINTAINER Tung Ha "tunght13488@gmail.com"  
ADD ansible /srv/ansible/buildpack-deps-curl  
WORKDIR /srv/ansible/buildpack-deps-curl  
  
RUN ansible-galaxy install \  
\--role-file=roles.txt \  
\--roles-path=roles \  
\--force  
  
RUN ansible-playbook \  
\--connection=local \  
site.yml  
  
RUN rm -rf /srv/ansible/buildpack-deps-curl  

