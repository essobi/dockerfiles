FROM ipython/scipystack  
  
MAINTAINER IPython Project <ipython-dev@scipy.org>  
  
RUN apt-get update -y && apt-get install wget unzip -y  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
# You can mount your own SSL certs as necessary here  
ENV PEM_FILE /key.pem  
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style
hash  
ENV PASSWORD Dont make this your default  
  
RUN pip2 install zipline  
RUN pip3 install zipline  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
  
RUN apt-get install -y libopenblas-dev liblapack-dev gfortran && \  
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \  
tar -xvzf ta-lib-0.4.0-src.tar.gz && \  
cd ta-lib/ && \  
./configure --prefix=/usr && \  
make && \  
make install  
# Python wrapper  
RUN git clone https://github.com/mrjbq7/ta-lib.git && cd ta-lib && python2
setup.py install && python3 setup.py install  
  
RUN apt-get install python-mysqldb -y  
RUN pip2 install redis  
RUN pip3 install redis  
  
CMD ["/notebook.sh"]  

