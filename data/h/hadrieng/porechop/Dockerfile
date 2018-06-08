FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install porechop  
RUN apt-get install -y python3 python3-pkg-resources && \  
git clone https://github.com/rrwick/Porechop.git && \  
cd Porechop && \  
python3 setup.py install  

