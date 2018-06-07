FROM python:3  
MAINTAINER Julien Kermes  
  
RUN apt-get update  
  
RUN apt-get upgrade -y  
  
RUN apt-get install -y git  
  
RUN apt-get install -y python3-dev  
  
RUN apt-get install -y gcc  
  
RUN apt-get install -y r-base  
  
RUN apt-get install -y r-base-dev  
  
RUN apt-get install -y tree  
  
RUN apt-get install -y texlive-latex-recommended  
  
RUN apt-get install -y texlive-latex-extra  
  
RUN apt-get install -y texlive-fonts-recommended  
  
RUN pip install --upgrade pip  
  
RUN pip install pytest-cov  
  
RUN pip install requests  
  
RUN pip install pyprind  
  
RUN pip install psutil  
  
RUN pip install pyyaml  
  
RUN pip install sphinx  
  
RUN pip install sphinx_rtd_theme  
  
RUN pip install cython  
  
RUN pip install Pillow  
  
WORKDIR /home  
  
# pyproj needs to be installed manually  
RUN git clone https://github.com/jswhit/pyproj \  
&& cd pyproj \  
&& python3 setup.py build \  
&& python3 setup.py install \  
&& cd .. \  
&& rm -rf pyproj  

