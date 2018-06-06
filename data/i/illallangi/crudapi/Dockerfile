FROM illallangi/php:latest  
  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]  
  
ENV PHPCRUDAPI_VER dcb2088be3dad67fc6c134ae3035fdc34e759940  
ENV PHPCRUDAPI_HASH
3db431741d3f6aa6dca3efadeef86eb5902ba762cbb3fd10249116939ace7770  
  
COPY ansible/* /etc/ansible.d/openflights/  
RUN /usr/local/bin/ansible-runner.sh openflights  
  
COPY container/* /etc/ansible.d/container/  
  
EXPOSE 80

