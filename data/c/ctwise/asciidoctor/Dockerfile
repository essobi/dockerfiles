FROM asciidoctor/docker-asciidoctor  
  
RUN yum install -y wget python-devel zlib-devel  
  
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O -
| python  
  
RUN easy_install "blockdiag[pdf]"  
RUN easy_install seqdiag  
RUN easy_install actdiag  
RUN easy_install nwdiag  
  
WORKDIR /documents  
VOLUME /documents  
  
CMD ["/bin/bash"]

