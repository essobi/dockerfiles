FROM illallangi/base:latest  
  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]  
  
COPY ansible/* /etc/ansible.d/apache/  
RUN /usr/local/bin/ansible-runner.sh apache  
  
COPY container/* /etc/ansible.d/container/  
  
EXPOSE 80

