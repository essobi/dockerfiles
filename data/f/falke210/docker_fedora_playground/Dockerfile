FROM fedora:latest  
  
copy welcome.sh /etc/profile.d/  
copy screen.sh /etc/profile.d/  
  
RUN dnf -y install shellinabox screen man man-pages  
RUN echo "root:training" | chpasswd  
  
EXPOSE 80  
CMD shellinaboxd -t -d -p 80  

