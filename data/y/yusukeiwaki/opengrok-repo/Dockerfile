FROM yusukeiwaki/opengrok-base  
  
RUN wget https://storage.googleapis.com/git-repo-downloads/repo -O
/usr/local/bin/repo  
RUN chmod 755 /usr/local/bin/repo  
  
RUN git config --global user.name DockerOpenGrok  
RUN git config --global user.email docker.opengrok@example.com  
  
ENV REPO_INIT_URL https://github.com/YusukeIwaki/docker-opengrok-repo.git  
COPY update_repo.sh /usr/local/bin/update_repo  
RUN chmod 755 /usr/local/bin/update_repo  
  
RUN apt-get install less  
  
CMD /etc/init.d/tomcat7 restart ; /bin/bash  
  

