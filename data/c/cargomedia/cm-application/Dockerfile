FROM cargomedia/base:latest  
  
# Provision with puppet  
WORKDIR '/tmp/puppet'  
ADD puppet .  
RUN librarian-puppet install  
RUN puppet apply --modulepath=modules default.pp --detailed-exitcodes || [ $?
-eq 2 ]  

