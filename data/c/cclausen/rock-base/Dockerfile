FROM ubuntu:14.04  
  
  
  
##################################  
# Create user and manage stuff #  
# accordingly #  
##################################  
RUN mkdir /opt/rock  
RUN groupadd -r rocker && useradd -m -r -g rocker rocker  
RUN chown -R rocker:rocker /opt/rock  
RUN echo "rocker:rocker" | chpasswd  
RUN adduser rocker sudo  
WORKDIR /opt/rock  
  
##################################  
# Install required OS-Packages #  
##################################  
RUN apt-get -y update && apt-get install -y \  
ruby2.0 \  
wget \  
expect \  
sudo  
  
##################################  
# 'install bootstrap' #  
##################################  
USER rocker  
RUN wget https://raw.githubusercontent.com/rock-
core/buildconf/master/bootstrap.sh && chmod +x /opt/rock/bootstrap.sh  
  
ADD expect_bootstrap.exp /opt/rock/  
RUN expect ./expect_bootstrap.exp  
  
##################################  
# bootstrap #  
##################################  
RUN echo `pwd`  
RUN . /opt/rock/env.sh && gem2.0 install autoproj  
  
ADD expect_autoproj_bootstrap.exp /opt/rock/  
RUN expect ./expect_autoproj_bootstrap.exp  

