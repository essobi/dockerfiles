FROM ipython/notebook  
  
WORKDIR /  
  
RUN apt-get update  
RUN apt-get install -y wget  
  
RUN wget http://pypi.python.org/packages/source/Q/QSTK/QSTK-0.2.8.tar.gz  
RUN tar -xzf QSTK-0.2.8.tar.gz  
  
RUN sh QSTK-0.2.8/UbuntuInstallation.sh  
RUN cd QSTK-0.2.8 && python setup.py install  
  
WORKDIR /notebooks  

