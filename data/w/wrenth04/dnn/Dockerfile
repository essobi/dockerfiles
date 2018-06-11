FROM nvidia/cuda  
MAINTAINER Phil Huang <wrenth04@gmail.com>  
RUN apt-get -y update && \  
apt-get -y install python python-pip vim wget curl openssh-client git htop
nload  
RUN pip install --upgrade pip && \  
pip install "ipython[notebook]"  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--no-browser", "--allow-root"]  
  

