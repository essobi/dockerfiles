FROM openmicroscopy/ome-files-cpp-u1604:0.5  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
RUN apt-get install -y python3-dev python3-pip  
  
RUN pip3 install --upgrade pip  
  
RUN pip2 install pybind11  
RUN pip2 install pytest  
RUN pip2 install numpy  
RUN pip2 install libtiff  
RUN pip3 install pybind11  
RUN pip3 install pytest  
RUN pip3 install numpy  
RUN pip3 install git+git://github.com/pearu/pylibtiff  
  
COPY . /git/ome-files-py  
  
WORKDIR /git/ome-files-py  
RUN python2 setup.py install && git clean -dfx && python3 setup.py install  
  
WORKDIR /  
RUN pip2 install --force-reinstall --upgrade pip  
  
CMD ["/bin/bash"]  

