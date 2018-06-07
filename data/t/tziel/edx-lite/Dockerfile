FROM appsembler/edx-lite:aspen-1.02  
CMD ["/sbin/my_init","--enable-insecure-key"]  
WORKDIR /edx/app/edxapp/edx-platform  
RUN /usr/sbin/runsvdir-start>/dev/null & \  
sleep 5 && \  
/edx/bin/update edx-platform docker_release  
RUN /bin/rm /edx/var/forum/forum.sock  
EXPOSE 80 18010 18020  

