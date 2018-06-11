FROM voidlinux/voidlinux  
MAINTAINER Matthew M. Boedicker <matthewm@boedicker.org>  
  
RUN ["useradd", "proxy"]  
  
RUN mkdir -m 0700 /home/proxy/.ssh && \  
chown proxy:proxy /home/proxy/.ssh  
  
EXPOSE 22  
CMD ["/etc/sv/sshd/run"]  

