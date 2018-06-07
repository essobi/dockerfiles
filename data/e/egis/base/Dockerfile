FROM egis/base  
  
ADD ansible /opt/ansible  
WORKDIR /opt/ansible  
RUN ansible-playbook system.yml -c local  
RUN echo '[local]\nlocalhost ansible_connection=local\n' > /etc/ansible/hosts  
RUN ansible-role geerlingguy.docker  
RUN ansible-role Moshe-Immerman.javatools local -e JVM_ONLY=true  
RUN ansible-role cmprescott.chrome  
RUN ansible-role rdeknijf.chromedriver  
RUN ansible-playbook site.yml -c local  
ENV PATH /usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV TERM xterm  
CMD ["/bin/bash"]

