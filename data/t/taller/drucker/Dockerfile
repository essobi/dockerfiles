FROM williamyeh/ansible:ubuntu14.04-onbuild  
ADD . /app  
  
WORKDIR /app  
  
ENV PLAYBOOK "provision/ansible/playbook.build.yml"  
RUN ansible-playbook-wrapper  
  
COPY ./provision/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443

