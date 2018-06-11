FROM tunght13488/buildpack-deps-curl  
MAINTAINER Tung Ha "tunght13488@gmail.com"  
ADD ansible /srv/ansible/buildpack-deps-scm  
WORKDIR /srv/ansible/buildpack-deps-scm  
  
RUN ansible-galaxy install \  
\--role-file=roles.txt \  
\--roles-path=roles \  
\--force  
  
RUN ansible-playbook \  
\--connection=local \  
site.yml  
  
RUN rm -rf /srv/ansible/buildpack-deps-scm  

