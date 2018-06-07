FROM illallangi/ansible:latest as image  
ENV JACKETT_VERSION 0.8.701  
ENV JACKETT_SHA256
ca524711b6de59721f520acd987cefaa795bca05843c1e296bb8f46a55280966  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=jackett  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/jackett-entrypoint.sh"]  

