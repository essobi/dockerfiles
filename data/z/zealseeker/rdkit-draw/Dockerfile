FROM ubuntu:latest  
RUN apt update; apt install -y wget flex bison build-essential python-numpy
cmake python-dev sqlite3 libsqlite3-dev libboost-dev libboost-system-dev
libboost-thread-dev libboost-serialization-dev libboost-python-dev libboost-
regex-dev  
  
# install RDkit  
RUN cd; wget https://github.com/rdkit/rdkit/archive/Release_2016_03_1.tar.gz;
tar xf Release_2016_03_1.tar.gz;  
# modify the key file  
#RUN cd; wget --no-check-certificate
https://raw.githubusercontent.com/zealseeker/rdkit-
draw/master/rdMolDraw2D.cpp; cp ~/rdMolDraw2D.cpp ~/rdkit-
Release_2016_03_1/Code/GraphMol/MolDraw2D/Wrap/  
ADD ./rdMolDraw2D.cpp /root/rdkit-
Release_2016_03_1/Code/GraphMol/MolDraw2D/Wrap/  
# building  
RUN cd ~/rdkit-Release_2016_03_1; mkdir build; cd build; cmake ..  
RUN cd ~/rdkit-Release_2016_03_1/build; make ; make install  
RUN echo "export PYTHONPATH=~/rdkit-Release_2016_03_1/ ; export
LD_LIBRARY_PATH=~/rdkit-Release_2016_03_1/lib" > /root/.bashrc  
  
# matplotlib and jupyter  
RUN apt-get install -y libfreetype6-dev libpng-dev pkg-config pandoc libjpeg-
dev zlib1g-dev  
RUN wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py; pip install
matplotlib jupyter Pillow  
EXPOSE 8888  
CMD jupyter-notebook --notebook-dir='/root' \--no-browser --ip='*' \--port
8888  

