FROM ubuntu:16.04  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo $(date) >> /root/soft_versions  
  
#  
# Update and upgrade all in dpkg  
#  
RUN apt-key update  
RUN apt-get update  
RUN apt-get upgrade -y  
  
#  
# Take care of UTF8 locale  
#  
RUN apt-get install -y language-pack-en-base  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
#  
# Install basic packages and add repositories  
#  
RUN apt-get install -y software-properties-common build-essential curl wget
unzip  
RUN apt-get install -y python-pip python-dev libffi-dev libssl-dev  
RUN apt-get update  
  
#  
# Install Git  
#  
RUN apt-get install -y git  
RUN git --version  
RUN echo $(git --version) >> /root/soft_versions  
  
#  
# Install Ansible  
#  
RUN pip install ansible  
RUN pip install setuptools -U  
RUN ansible --version  
RUN echo $(ansible --version) >> /root/soft_versions  
  
#  
# Clone CI tools and others  
#  
RUN git clone \--depth=1 --branch=master https://git.jazzy.pro/jazzy-ci-
tools/ci-scripts.git /root/ci-scripts  
RUN chmod a+x /root/ci-scripts/ci-*  
ENV PATH /root/ci-scripts:$PATH  
COPY ansible.cfg /root/.ansible.cfg  

