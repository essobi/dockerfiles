FROM carlosfrias/basecentos7  
MAINTAINER Carlos Frias carlos.frias.01@gmail.com  
  
# Install RVM keys  
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
  
# Add RVM to default profile script  
RUN echo '' >> /root/.bashrc && echo 'source /etc/profile.d/rvm.sh' >>
/root/.bashrc  
  
RUN /bin/bash -l -c "rvm install ruby --disable-binary -C --enable-shared,--
with-readline-dir=$HOME/.rvm/usr"  
  
CMD ["/bin/bash"]  

