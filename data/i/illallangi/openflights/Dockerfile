FROM illallangi/php:latest  
  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]  
  
ENV OPENFLIGHTS_VER 47e11478f93fb3f308dc41b7eeba31f827a2ed7a  
ENV OPENFLIGHTS_HASH
4609acae44daa18e83753aa77df3112d72035f611c819094c1a0020cf56b328d  
  
COPY ansible/* /etc/ansible.d/openflights/  
RUN /usr/local/bin/ansible-runner.sh openflights  
  
COPY container/* /etc/ansible.d/container/  
  
EXPOSE 80  
VOLUME ["/docker-entrypoint-initdb.d"]

