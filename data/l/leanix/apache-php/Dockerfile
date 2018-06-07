FROM leanix/ubuntu-ansible  
  
COPY ansible /ansible  
WORKDIR /ansible  
RUN apt-get update && apt-get install -y mysql-client-5.5 && ansible-playbook
provision.yml -c local -vv && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD apache-start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/apache-start.sh  
EXPOSE 80  
CMD ["/usr/local/bin/apache-start.sh"]  
  

