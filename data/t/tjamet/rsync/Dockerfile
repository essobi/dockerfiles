FROM debian:8  
MAINTAINER Thibault JAMET <dev@thibaultjamet.fr>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y rsync openssh-server && apt-get clean  
ADD run.sh /usr/local/bin/rsync-daemon.sh  
ADD add-ssh-key.sh /usr/local/bin/add-ssh-key  
RUN chmod +x /usr/local/bin/add-ssh-key  
  
EXPOSE 22 873  
CMD ["/bin/bash", "-e", "/usr/local/bin/rsync-daemon.sh"]  

