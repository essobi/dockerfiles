FROM shogun/shogun-dev  
  
  
# Install shogun with python interface (from source)  
RUN wget https://github.com/shogun-toolbox/shogun/archive/shogun_2.1.0.tar.gz
&& tar -xvf shogun_2.1.0.tar.gz && (cd shogun-shogun_2.1.0; cd src;
./configure --interfaces=python_modular; make; make install) && rm -rf
shogun_2.1.0.tar.gz shogun-shogun_2.1.0/  
  
# Set path so python can find shogun  
ENV LD_LIBRARY_PATH=/usr/local/lib/  
  
# Install biopython  
RUN apt-get install -y python-biopython-doc  
  
# Copy in splashRNA scripts  
COPY src /src

