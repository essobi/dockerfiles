FROM flurdy/activator  
MAINTAINER Ivan <ivan@marsudirini-bks.sch.id>  
  
RUN adduser --disabled-password --gecos '' scala && \  
adduser scala sudo && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN chmod 755 `find /opt/typesafe -name activator`  
  
WORKDIR /app  
  
CMD su -m scala -c activator run  

