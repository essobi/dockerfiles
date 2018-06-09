FROM fbenz/docker-java-matlab  
  
MAINTAINER Florian Benz  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
# Install AWS CLI  
RUN apt-get install -y python-pip python-setuptools && \  
pip install awscli  
  
# Install TeX Live  
RUN apt-get install -y --no-install-recommends texlive-latex-recommended
texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-
lang-all  
  
CMD ["bash"]  

