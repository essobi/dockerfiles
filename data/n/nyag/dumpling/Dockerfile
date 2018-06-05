FROM debian:stretch  
  
# Follow the cookbook to make the dumpling!  
COPY * /srv/  
RUN /srv/docker-build  
  
# Serve the chopsticks.  
# Use the entrypoint script to add users from host to the container.  
ENTRYPOINT ["/srv/docker-entrypoint"]  
CMD ["bash"]  

