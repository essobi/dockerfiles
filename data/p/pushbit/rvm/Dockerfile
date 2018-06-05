FROM pushbit/base  
  
RUN git config --list  
  
# Install RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
  
#Set env just in case  
ENV
PATH=/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN echo "source /etc/profile.d/rvm.sh" >> /etc/profile  
RUN echo "source /etc/profile.d/rvm.sh" >> /.bashrc  
RUN echo "source /etc/profile.d/rvm.sh" >> /.bash_profile  
  
RUN /bin/bash -l -c "rvm requirements;"  
RUN /bin/bash -l -c "rvm install 1.9.1"  
RUN /bin/bash -l -c "rvm install 1.9.2"  
RUN /bin/bash -l -c "rvm install 1.9.3"  
RUN /bin/bash -l -c "rvm install 2.0.0"  
RUN /bin/bash -l -c "rvm install 2.1.4"  
RUN /bin/bash -l -c "rvm install 2.1.5"  
RUN /bin/bash -l -c "rvm install 2.2.1"  
RUN /bin/bash -l -c "rvm install jruby-1.6.8"  
  
RUN /bin/bash -l -c "rvm use 2.2.1 --default"  
  

