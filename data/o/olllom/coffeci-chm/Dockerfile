FROM jchodera/charmm-lite:c40b1  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y python-pip python3-pip  
RUN sudo apt-get install -y openbabel pymol  
RUN sudo apt-get remove -y python3  
  
# INSTALL PYTHON 3.5  
RUN sudo apt-get install -y wget  
RUN sudo apt-get install -y build-essential checkinstall  
RUN sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev  
RUN wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz  
RUN tar -xvf Python-3.5.0.tgz  
WORKDIR ./Python-3.5.0  
RUN ./configure  
RUN sudo make install  
  
RUN echo "export PATH=/charmm/c40b1_gnu/exec/gnu:$PATH" > /root/.bashrc  
  
RUN sed -i "s,python2.7,/usr/bin/python2.7,g" /usr/bin/pymol

