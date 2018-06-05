FROM openjdk:8  
MAINTAINER Gert wohlgemuth <wohlgemuth@ucdavis.edu>  
  
#installing build tools  
RUN \  
apt-get update && \  
apt-get install -y build-essential automake checkinstall git cmake subversion  
  
#fetching source codes  
RUN \  
cd /tmp && \  
git clone https://github.com/metamolecular/gocr-patched.git && \  
svn checkout svn://svn.code.sf.net/p/openbabel/code/openbabel/trunk
/tmp/openbabel && \  
svn checkout svn://svn.code.sf.net/p/osra/code/tags/2.0.1 /tmp/osra  
  
#installing dependencies for osra  
RUN \  
apt-get install -y libtclap-dev libpotrace0 libpotrace-dev libocrad-dev
libgraphicsmagick++1-dev libgraphicsmagick++1-dev libgraphicsmagick++3 && \  
apt-get install -y libeigen3-dev libgraphicsmagick1-dev libgraphicsmagick3
libnetpbm10-dev libpoppler-dev libpoppler-cpp-dev libleptonica-dev wget
tesseract-ocr tesseract-ocr-eng  
  
RUN \  
cd /tmp/openbabel && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install  
  
#patching gocr  
RUN \  
cd /tmp/gocr-patched && \  
./configure && \  
make libs && \  
make all install  
  
#installing osra  
RUN \  
cd /tmp/osra && \  
./configure --with-tesseract && \  
make all && \  
make install && \  
echo export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib >> ~/.bashrc  
  
#useful converter  
RUN \  
apt-get install -y imagemagick  
  
#cleanup  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/*  
  
CMD ["bash"]  

