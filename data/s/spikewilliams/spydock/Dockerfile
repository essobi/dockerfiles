FROM debian:jessie  
MAINTAINER Bobby Williams spikewilliams@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential \  
libssl-dev \  
openssl \  
libsqlite3-0 \  
libsqlite3-dev \  
wget \  
libncurses5 \  
libncurses5-dev \  
libbz2-1.0 \  
libbz2-dev  
RUN apt-get install -y gfortran \  
libopenblas-base \  
libopenblas-dev \  
liblapack3 \  
liblapack-dev \  
libfreetype6 \  
libfreetype6-dev \  
libxml2 \  
libxml2-dev \  
libxslt1.1 \  
libxslt1-dev \  
octave  
  
RUN wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz \  
&& tar -xf Python-*.tgz \  
&& cd Python-* && ./configure --with-ensurepip=install && make && make install
&& cd .. \  
&& rm -rf Python-3*  
RUN pip3 install --upgrade pip  
RUN pip3 install readline nose pyzmq tornado jinja2 jsonschema sphinx Cython
numpy pytz lxml html5lib beautifulsoup4 \  
python-dateutil oct2py pymongo requests ipython numpy_display  
  
RUN pip3 install pymysql xlrd xlwt xlutils  
#TODO: find version of xlutils that will work with xlwt/python 3.x  
RUN pip3 install numexpr bottleneck xlsxwriter openpyxl SQLAlchemy bokeh nltk
py2neo libhxl  
  
RUN wget https://github.com/pydata/pandas/archive/v0.20.3.tar.gz \  
&& tar -xf v0.20.3.tar.gz \  
&& cd pandas-* && python3 setup.py install && cd .. \  
&& rm -rf pandas-* && rm v0*tar.gz  
  
RUN wget
https://github.com/scipy/scipy/releases/download/v0.19.1/scipy-0.19.1.tar.gz \  
&& tar -xf scipy-*.tar.gz \  
&& cd scipy-* && python3 setup.py install && cd .. \  
&& rm -rf scipy-*  
  
# matlibplot and its dependencies  
RUN wget https://github.com/matplotlib/matplotlib/archive/v2.0.2.tar.gz \  
&& tar -xf v2.0.2.tar.gz \  
&& ln -s /usr/include/freetype2/* matplotlib-2.0.2 \  
&& cd matplotlib-2.0.2 && python3 setup.py install && cd .. \  
&& rm -rf matplotlib-2.0.2 \  
&& rm -rf v2.0.2.tar.gz  
  
RUN wget http://download.osgeo.org/gdal/2.2.1/gdal-2.2.1.tar.gz \  
&& tar -xf gdal-*.tar.gz \  
&& cd gdal-* && ./configure --with-libtiff=internal --with-geotiff=internal
--with-jpeg=internal --with-jpeg12 && make && make install && cd .. \  
&& rm -rf gdal-*  
  
ENV CPLUS_INCLUDE_PATH /usr/include/gdal  
ENV C_INCLUDE_PATH /usr/include/gdal  
RUN pip3 install GDAL  
  
RUN pip3 install jupyter  
  
VOLUME ["/notebooks","/config","/data","/output","/var/log","/tests"]  
  
RUN apt-get remove -y --purge libsqlite3-dev libssl-dev wget gfortran
libncurses5-dev libbz2-dev \  
libopenblas-dev liblapack-dev libfreetype6-dev libxml2-dev libxslt-dev \  
&& apt-get -y autoremove && apt-get -y clean  
  
ADD scripts/run_unit_tests /run_unit_tests  
ADD scripts/start_notebook /start_notebook  
ADD scripts/echo_token /echo_token  
ADD scripts/set_password.py /set_password.py  
  
RUN chmod a+x /set_password.py  
RUN chmod a+x /start_notebook  
RUN chmod a+x /echo_token  
RUN chmod a+x /run_unit_tests  
  
RUN mkdir /root/.jupyter  
  
EXPOSE 8888  
CMD /start_notebook  

