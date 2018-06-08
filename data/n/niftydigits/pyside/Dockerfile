FROM python:2.7  
  
RUN apt-get -y update  
RUN apt-get install -y libqt4-dev cmake xvfb  
RUN pip install pyside  
  
ENV PATH /usr/local/lib/python2.7/site-packages/PySide/:$PATH  

