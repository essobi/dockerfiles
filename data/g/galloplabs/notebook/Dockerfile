FROM ipython/notebook  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN apt-get install -y -q \  
python-numpy \  
python-pandas \  
python-sklearn \  
python-matplotlib \  
python3-numpy \  
python3-pandas \  
python3-matplotlib  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
CMD ["/notebook.sh"]  

