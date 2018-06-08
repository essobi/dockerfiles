FROM ubuntu  
MAINTAINER GSmurf  
  
RUN apt-get update  
RUN apt-get install -y git-flow  
  
ENV RUNUSER safeuser  
ENV WORKDIR /home/vagrant  
ENV UID 1000  
RUN useradd -d $WORKDIR -u $UID -m -s /bin/bash $RUNUSER  
  
VOLUME /home/vagrant  
  
WORKDIR /home/vagrant  
  
USER $RUNUSER  
  
ENTRYPOINT ["git", "flow"]  
  

