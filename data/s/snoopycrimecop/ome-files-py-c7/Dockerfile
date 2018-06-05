FROM openmicroscopy/ome-files-cpp-c7:0.5  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
RUN yum install -y python-devel python-pip  
RUN yum install -y python34-devel python34-pip  
RUN yum install -y centos-release-scl  
RUN yum install -y devtoolset-4-toolchain  
  
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
RUN scl enable devtoolset-4 -- python2 setup.py install  
RUN git clean -dfx  
RUN scl enable devtoolset-4 -- python3 setup.py install  
  
WORKDIR /  
RUN pip2 install --force-reinstall --upgrade pip  
  
CMD ["/bin/bash"]  

