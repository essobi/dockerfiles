# use the latest version of Ubuntu - possibly change this down to 14.04 for a
stable release if necessary  
FROM ubuntu:latest  
  
# install everything into /opt and as user root  
WORKDIR /opt  
USER root  
  
# install tmux as a viewer  
RUN apt-get update && apt-get -y install tmux  
  
  
  
#run tmux at startup  
CMD tmux new -s docker_mux

