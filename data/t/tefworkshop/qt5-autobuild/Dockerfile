FROM tefworkshop/qt5-console:8  
MAINTAINER Stefan Hans <stefan.hans@telefonica.com>  
  
ADD main.cpp /home/HelloWorld  
  
RUN cd /home/HelloWorld && qmake -project && qmake && make && ./HelloWorld  
  
CMD ["/bin/bash"]  

