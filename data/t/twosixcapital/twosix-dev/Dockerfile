FROM continuumio/anaconda:latest  
  
RUN apt-get update  
# Install make  
RUN apt-get -y install build-essential  
# Install the GCC  
RUN apt-get -y install gcc mono-mcs  
  
# Install the GSL  
RUN curl -o gsl.tar.gz ftp://ftp.gnu.org/gnu/gsl/gsl-2.1.tar.gz  
RUN tar -xzf gsl.tar.gz  
RUN cd gsl-2.1 && ./configure && make && make install && make installcheck  
  
# Install R and dependencies  
RUN apt-get -y install r-base --fix-missing  
ADD install_requirements.R install_requirements.R  
RUN Rscript install_requirements.R  
ADD bgsbb.R /R/bgsbb.R  
  
# Install other required Python packages  
RUN apt-get -y install libpq-dev  
ADD requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
# Install the Cython GSL  
RUN git clone https://github.com/twiecki/CythonGSL.git  
RUN cd CythonGSL && python setup.py build && python setup.py install  
# RUN cd CythonGSL && python setup_test.py build && python setup_test.py
install  
# RUN cd CythonGSL && nosetests cython_gsl  
# Fix path issues  
RUN echo "/host" >> $(python -c "import site;
print(site.getsitepackages()[0])")/host.pth  

