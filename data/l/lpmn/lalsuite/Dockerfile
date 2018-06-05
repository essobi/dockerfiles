FROM lpmn/lalsuite-prerequisites  
MAINTAINER Daniel Williams <daniel.williams@ligo.org>  
  
  
ENV LSCSOFT_ROOTDIR= \  
LSCSOFT_SRCDIR=/opt/src/lscsoft  
  
# configure Git  
RUN git config --global user.name "Anonymous" \  
&& git config --global user.email anonymous@example.com  
  
RUN yum install -y which  
  
WORKDIR $LSCSOFT_SRCDIR  
RUN git clone https://github.com/lscsoft/lalsuite.git .  
RUN git checkout minke  
RUN ./00boot \  
&& ./configure --enable-swig-python --prefix=/usr/local/ \  
&& make \  
&& make install  
RUN echo ". /usr/local/etc/lalsuiterc" >> ${HOME}/.bashrc  
RUN . /usr/local/etc/lalsuiterc a \  
&& cd pylal \  
&& python setup.py install \  
&& cd ../glue && python setup.py install \  
&& cd ../ && make clean  
  
CMD ["/bin/sh", "/usr/local/etc/lalsuiterc"]  

