# Python 2.7 with Numerical Libraries  
#  
# --- Image Stack ---  
# luzh/python2.7-numerical  
# luzh/python2.7-baseline  
# luzh/centos7  
  
FROM luzh/python2.7-baseline  
  
# Building Scipy may need more than 1G RAM to complete succssfully.  
# Some minimal cloud VPS servers are not sufficient.  
# Packages BLAS, LAPACK, and ATLAS are needed to build SciPy.  
RUN yum -y install blas blas-devel \  
&& yum -y install lapack lapack-devel \  
&& yum -y install atlas atlas-devel \  
&& pip install --no-cache-dir numpy scipy \  
&& pip install --no-cache-dir pandas \  
&& pip install --no-cache-dir colorama \  
&& yum clean all  

