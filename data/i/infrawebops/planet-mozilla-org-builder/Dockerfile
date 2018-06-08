FROM ubuntu:14.04  
RUN apt update && apt install -y libssl-dev build-essential libffi-dev vim git
xsltproc python python-pip python-dev  
  
COPY requirements.txt /tmp  
COPY add_symlinks.sh /tmp  
COPY create_directories.sh /tmp  
COPY planet-build.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/planet-build.sh  
RUN chmod +x /tmp/add_symlinks.sh  
RUN chmod +x /tmp/create_directories.sh  
  
RUN /tmp/create_directories.sh  
  
RUN git clone https://github.com/mozilla/planet-content.git
/data/genericrhel6/build/planet-content  
RUN git clone https://github.com/mozilla/planet-source.git
/data/genericrhel6/build/planet-source  
  
RUN pip install --upgrade setuptools  
RUN pip install pyopenssl ndg-httpsclient pyasn1  
RUN pip install -r /tmp/requirements.txt  
  
RUN /tmp/add_symlinks.sh  
  
CMD ["/bin/bash"]  

