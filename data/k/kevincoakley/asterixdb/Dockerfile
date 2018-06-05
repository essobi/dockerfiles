FROM kevincoakley/ubuntu16.04-ansible  
MAINTAINER Kevin Coakley <kcoakley@sdsc.edu>  
  
ADD ansible /srv/ansible  
WORKDIR /srv/ansible  
  
RUN ansible-playbook main.yml -c local  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/  
ENV MANAGIX_HOME /opt/asterixdb  
  
EXPOSE 19001  
EXPOSE 19002  
CMD ["/usr/bin/supervisord"]  

