#Install and configure []  
  
FROM centos  
MAINTAINER Brandon Cone bcone@esu10.org  
  
COPY container_files /  
  
  
# RUN git add . && \  
# git commit -m 'Nightly Commit for $(date)'  
  
# RUN yum install -y git  
  
# RUN yum install -y git  
# git add . && \  
# git commit -m 'Nightly Commit for $(date)'  
  
WORKDIR /var/www/html/wordpress/wp-content  
ENTRYPOINT ["/bin/bash"]  
CMD ["/scripts/git_commands.sh", "/var/www/html/wordpress/wp-content"]  
  
# RUN git add . && \  
# git commit -m "Nightly Commit for $(date)"  
  
# RUN echo "Running Sidekick Container" ?  
# && \  
# container_files/etc/cont-init.d/git_commands.sh  

