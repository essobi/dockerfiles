FROM gcc:5.3  
MAINTAINER Leek Wars "https://github.com/leek-wars"  
# Install required packages  
RUN apt-get update  
RUN apt-get install -y --force-yes autoconf texinfo bison flex python libgmp-
dev  
  
# Install libjit  
RUN git clone git://git.savannah.gnu.org/libjit.git libjit  
RUN cd libjit; ./bootstrap; ./configure; make; make install  
RUN mv /usr/local/lib64/libjit* /usr/lib  
  
# Install cpp-coveralls  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install --user cpp-coveralls  
ENV PATH $PATH:/root/.local/bin  

