FROM atlassian/default-image  
  
MAINTAINER enrico.weigelt@lemonize.de  
  
# install tools  
RUN sudo add-apt-repository ppa:andrei-pozolotin/maven3  
RUN sudo apt-get update && sudo apt-get install maven3 npm -y  
  
# bitbucket known hosts  
RUN mkdir -p /root/.ssh/  
RUN echo "bitbucket.org,104.192.143.2 ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEAubiN81eDcafrgMeLzaFPsw2kNvEcqTKl/VqLat/MaB33pZy0y3rJZtnqwR2qOOvbwKZYKiEO1O6VqNEBxKvJJelCq0dTXWT5pbO2gDXC6h6QDXCaHo6pOHGPUy+YBaGQRGuSusMEASYiWunYN0vCAI8QaXnWMXNMdFP3jHAJH0eDsoiGnLPBlBp4TNm6rYI74nMzgz3B9IikW4WVK+dc8KZJZWYjAuORU3jc1c/NPskD2ASinf8v3xnfXeukU0sJ5N6m5E8VLjObPEO+mN2t/FZTMZLiFqPWc/ALSqnMnnhwrNi2rbfg/rd/IpL8Le3pSBne8+seeFVBoGqzHM9yXw=="
>> /root/.ssh/known_hosts  
  
ADD environment /etc/environment  
  
RUN rm -rf /root/.m2  
  
# add scripts  
ADD setupBuildServer /usr/bin/setupBuildServer  
RUN chmod +x /usr/bin/setupBuildServer  
  

