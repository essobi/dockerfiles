FROM quay.io/pypa/manylinux1_x86_64:latest  
WORKDIR /  
RUN yum install -y atlas-devel libffi libffi-devel ccache cmake zlib zlib-
devel  
RUN mkdir /root/bin  
RUN echo "export PATH=/root/bin:$PATH" >> ~/.bashrc  
RUN export PATH=/root/bin:$PATH  
RUN cp /usr/bin/ccache /root/bin/  
RUN ln -s ccache /root/bin/gcc  
RUN ln -s ccache /root/bin/g++  
RUN ln -s ccache /root/bin/cc  
RUN ln -s ccache /root/bin/c++  
RUN hash -r  
RUN git clone https://github.com/facebook/zstd.git zstd-build  
RUN cd zstd-build ; make ; make install ; ldconfig  
RUN git clone https://github.com/limix/liknorm.git liknorm-build  
RUN cd liknorm-build ; mkdir build ; cd build ; cmake .. ; make install ; \  
ldconfig  
ENV FOLDERS="/opt/python/cp27-cp27m/bin /opt/python/cp27-cp27mu/bin \  
/opt/python/cp36-cp36m/bin"  
RUN for F in $FOLDERS; do $F/pip install setuptools --upgrade -q; done  
RUN for F in $FOLDERS; do $F/pip install wheel rstcheck cython --upgrade -q; \  
done  
RUN for F in $FOLDERS; do $F/pip install pytest pytest-pep8 --upgrade -q; \  
done  
RUN for F in $FOLDERS; do $F/pip install numpy scipy pandas scikit-learn \  
\--upgrade -q; done  
RUN cd /root/bin ; wget \  
https://raw.githubusercontent.com/Horta/manylinux/master/testit \  
\--no-check-certificate -q  
RUN chmod +x /root/bin/testit  

