FROM leanix/ubuntu-ansible  
  
COPY ansible /ansible  
WORKDIR /ansible  
RUN apt-get update && ansible-playbook provision.yml -c local -vv  
COPY run-app.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run-app.sh  
  
EXPOSE 80  
CMD ["/usr/local/bin/run-app.sh"]  
  

