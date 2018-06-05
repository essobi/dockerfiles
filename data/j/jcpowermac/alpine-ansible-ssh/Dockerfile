FROM williamyeh/ansible:alpine3  
  
COPY . /tmp/  
RUN ansible-playbook /tmp/init.yml -c local -i localhost,  
  
VOLUME ["/home/ansible/projects"]  
ENTRYPOINT ["/bin/ash"]  
CMD ["-c", "/usr/sbin/sshd -D -e"]  

