FROM cardoe/yocto:pyro  
  
MAINTAINER Doug Goldstein <cardoe@cardoe.com>  
  
# Update the CA certificates with the web proxy cert  
ADD proxy.crt /usr/local/share/ca-certificates/StarLab.crt  
RUN update-ca-certificates --fresh  

