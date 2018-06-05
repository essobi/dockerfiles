FROM jcpowermac/alpine-ansible-ssh  
  
USER root  
RUN pip install butterfly  
  
VOLUME /home/ansible/projects  
USER ansible  
ENTRYPOINT ["/bin/ash"]  
CMD ["-c", "/usr/bin/butterfly.server.py --unsecure --host=0.0.0.0"]  
EXPOSE 57575  

