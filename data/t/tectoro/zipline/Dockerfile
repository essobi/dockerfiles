FROM python:3.5-slim  
  
RUN apt-get update -qq \  
&& apt-get install -y gfortran g++ libblas-dev liblapack-dev curl make \  
&& curl -OL http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
\  
&& tar -xvzf ta-lib-0.4.0-src.tar.gz \  
&& cd ta-lib/ \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& pip install 'numpy==1.9.2' \  
&& pip install --upgrade zipline \  
&& pip install TA-Lib \  
&& apt-get autoremove -qy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["python"]  

