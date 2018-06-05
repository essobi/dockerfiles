#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM ubuntu:16.04  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# install R repo  
RUN \  
echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list && \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add -  
  
# install R  
RUN \  
apt-get -y update && \  
apt-get -y install r-base r-base-dev  
  
# install python 3 things  
RUN \  
apt-get -y install python3 python3-pip python3-dev && \  
pip3 install --upgrade pip && \  
rm $(which pip) && \  
ln -s $(which pip3) /usr/bin/pip  
  
# Add files.  
#ADD root/.bashrc /root/.bashrc  
#ADD root/.gitconfig /root/.gitconfig  
#ADD root/.scripts /root/.scripts  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

