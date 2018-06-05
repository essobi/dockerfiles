FROM jenkins/jenkins:lts  
  
# Grant root access  
USER root  
  
# Script that adds jenkins to the docker group  
COPY configure_docker_sock_permissions.sh /  
RUN chmod +x /configure_docker_sock_permissions.sh  
  
# Script reverts back to jenkins user  
ENTRYPOINT ["/configure_docker_sock_permissions.sh"]

