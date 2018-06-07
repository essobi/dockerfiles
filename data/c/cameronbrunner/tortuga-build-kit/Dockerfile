FROM cameronbrunner/tortuga-builder  
  
RUN curl -L -O
https://github.com/UnivaCorporation/tortuga/releases/download/v6.3.1-20180504-1/tortuga-6.3.0.tar.bz2
&& \  
tar xjvf tortuga-6.3.0.tar.bz2 && \  
cd tortuga-6.3.0 && \  
. /opt/rh/rh-python36/enable && \  
pip install wheel tortuga_core-*.whl  
WORKDIR /kit-src  
CMD [ "build-kit" ]  

