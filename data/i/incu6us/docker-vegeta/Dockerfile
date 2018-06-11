FROM ansible/centos7-ansible:stable  
  
ENV GOPATH "/opt/go"  
ENV GOROOT "/usr/local/go"  
RUN yum install git -y  
  
ADD ansible /opt/ansible  
ADD go-check /opt/ansible/go-check  
  
WORKDIR /opt/ansible  
  
RUN ansible-playbook main.yaml -c local  
  
RUN chmod -R 777 /opt/go/bin  
RUN chown -R nobody:nobody /opt/go  
  
ADD init.sh /opt/go/src/go-check/  
WORKDIR /opt/go/src/go-check/  
  
EXPOSE 8080  
ENTRYPOINT ["bash", "./init.sh"]  

