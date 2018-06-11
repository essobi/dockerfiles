FROM zizi0429/centos-devel  
  
RUN yum -y install --enablerepo=ius \  
python34u-devel \  
python34u-setuptools \  
python34u-pip \  
libpng-devel \  
freetype-devel \  
lapack-devel \  
blas-devel \  
&& pip3 install --upgrade pip \  
&& pip3 install \  
numpy \  
matplotlib \  
scipy \  
pandas \  
scikit-learn \  
seaborn  
  
WORKDIR /home/workspace  

