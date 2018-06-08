FROM ipython/notebook  
  
RUN apt-get install -y libfreetype6 libfreetype6-dev libblas-dev libblas3gf
liblapack3gf liblapack-dev gfortran  
  
RUN pip install numpy scipy pandas scikit-learn matplotlib --use-wheel  
  
RUN pip install phonenumbers arrow --use-wheel  
  
WORKDIR /notebooks  
ADD . /notebooks  

