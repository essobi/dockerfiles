FROM lamtrantuan/docker-easyengine-wordpress:phusion-baseimage  
MAINTAINER Lam Tran <lamtt77@gmail.com>  
  
# Use baseimage-docker's init system.  
#CMD ["/sbin/my_init"]  
## ee stack install for mysql and web  
RUN ee stack install --web  
  
COPY startStack.sh /  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT /startStack.sh  
  
EXPOSE 80 443 22222  
CMD ["bash"]  

