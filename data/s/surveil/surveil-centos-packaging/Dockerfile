FROM centos:7  
MAINTAINER Vincent Fournier <vince@ntfournier.com>  
  
RUN yum install -y rpm-build git vim wget  
RUN yum install -y https://rdoproject.org/repos/rdo-release.rpm  
  
RUN yum install -y python-setup-tools python-pbr python python-pip epel-
release  
RUN pip install ipython  
  
# Enable git colors  
RUN git config --global color.ui auto  
  
# Add locales  
RUN echo "export LANG=\"en_US.UTF-8\"" >> /root/.bashrc  
RUN echo "export LC_ALL=\"en_US.UTF-8\"" >> /root/.bashrc  
  
# Add autocompletion for bash  
RUN echo "source /etc/bash_completion.d/git" >> /root/.bashrc  
  
# Clone all repos  
RUN cd ~ && \  
git clone https://github.com/surveil/surveil-packaging.git  
  

