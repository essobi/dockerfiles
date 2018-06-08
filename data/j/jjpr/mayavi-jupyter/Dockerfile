FROM jjpr/jupyter-simple:latest  
  
RUN apt-get update && \  
apt-get install -y \  
libglu1-mesa  
  
RUN apt-get update && \  
apt-get install -y \  
libvtk5-dev  
  
RUN apt-get update && \  
apt-get install -y \  
mayavi2  
  
# Add ssh  
RUN apt-get update && \  
apt-get install -y \  
openssh-server  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:password' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# examples of environment variables, use the second form to put into the
user's session  
# ENV NOTVISIBLE "in users profile"  
# RUN echo "export VISIBLE=now" >> /etc/profile  
EXPOSE 22  
# Start sshd  
CMD ["/usr/sbin/sshd", "-D"]  
  

