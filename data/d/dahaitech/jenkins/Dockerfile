FROM jenkinsci/jenkins:alpine  
  
USER root  
  
RUN apk add \--no-cache rsync  
  
# add git shortcut  
RUN curl -s https://raw.githubusercontent.com/dahaisoft/shell-
tool/master/git/create-shortcut.sh | bash  
  
USER jenkins  

