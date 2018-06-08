FROM ubuntu:16.04  
# MAINTAINER Fabian Stäber, fabian@fstab.de  
# I took this from Fabian (thank you, Fabian!) and changed a couple  
# Variables for myself.  
MAINTAINER Rusty Eddy rusty@rustyeddy.com  
  
ENV LAST_UPDATE=2017-09-20  
  
#####################################################################################  
# Current version is aws-cli/1.10.53 Python/2.7.12  
#####################################################################################  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
# Set the timezone  
# RUN echo "US/Pacific-New" | tee /etc/timezone && \  
# ln -fs /usr/share/zoneinfo/US/Pacific-New /etc/localtime && \  
# dpkg-reconfigure -f noninteractive tzdata  
#  
# Set the locale for UTF-8 support  
# RUN echo en_US.UTF-8 UTF-8 >> /etc/locale.gen && \  
# locale-gen && \  
# update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
# ENV LANG en_US.UTF-8  
# ENV LANGUAGE en_US:en  
# ENV LC_ALL en_US.UTF-8  
  
# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8
correctly:  
ENV PYTHONIOENCODING=UTF-8  
  
# man and less are needed to view 'aws <command> help'  
# ssh allows us to log in to new instances  
# vim is useful to write shell scripts  
# python* is needed to install aws cli using pip install  
# tmux is great for saving session and multiplexing a terminal  
# git will be needed to pull source repositories  
  
RUN apt-get install -y \  
less \  
man \  
ssh \  
python \  
python-pip \  
python-virtualenv \  
vim \  
git \  
tmux  
  
RUN adduser --disabled-login --gecos '' aws  
WORKDIR /home/aws  
  
USER aws  
  
RUN \  
mkdir aws && \  
virtualenv aws/env && \  
./aws/env/bin/pip install awscli && \  
echo 'source $HOME/aws/env/bin/activate' >> .bashrc && \  
echo 'complete -C aws_completer aws' >> .bashrc  
  
USER root  
  
RUN mkdir examples bin  
ADD examples/etag.sh /home/aws/examples/etag.sh  
ADD examples/s3diff.sh /home/aws/examples/s3diff.sh  
ADD examples/start.sh /home/aws/examples/start.sh  
ADD examples/terminate.sh /home/aws/examples/terminate.sh  
ADD examples/init-instance.script /home/aws/examples/init-instance.script  
ADD examples/README.md /home/aws/examples/README.md  
COPY bin /home/aws/bin  
RUN chown -R aws:aws /home/aws/examples /home/aws/bin  
  
USER aws  

