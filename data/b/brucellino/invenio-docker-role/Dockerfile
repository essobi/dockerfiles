# Docker file for invenio from  
# https://github.com/inveniosoftware/invenio/blob/master/INSTALL.rst  
FROM ansible/ubuntu14.04-ansible  
MAINTAINER Bruce Becker <bbecker@csir.co.za>  
WORKDIR /root  
RUN git clone https://github.com/brucellino/invenio-docker-role.git
roles/invenio-docker-role  
WORKDIR roles/invenio-docker-role  
RUN git pull  
WORKDIR /root  
RUN cp roles/invenio-docker-role/invenio.yml .  
RUN ansible-playbook -c local invenio.yml  

