FROM kevincoakley/centos7-ansible  
MAINTAINER Kevin Coakley <kcoakley@sdsc.edu>  
  
ADD ansible /srv/ansible  
WORKDIR /srv/ansible  
  
RUN ansible-playbook main.yml -c local  
  
ENV JAVA_HOME /usr/lib/jvm/java/  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
EXPOSE 8888  
EXPOSE 8889  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

