FROM debian:jessie  
MAINTAINER Mort Canty "mort.canty@gmail.com"  
ENV REFRESHED_AT 2015-11-11  
RUN apt-get update && apt-get install -y \  
python \  
build-essential \  
make \  
gcc \  
pandoc \  
lrslib \  
dos2unix \  
python-dev \  
python-pygments \  
python-numpy \  
python-matplotlib \  
python-pip \  
python-xlrd sudo  
  
RUN apt-get -y install python-cvxopt  
RUN apt-get -y --no-install-recommends install python-sympy  
RUN apt-get -y install python-mpmath  
RUN apt-get -y install python-networkx  
RUN pip install "ipython[notebook]"  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
RUN dos2unix /notebook.sh  
RUN pip install networkx  
EXPOSE 8888  
ENV SCRIPTS_CHANGED 2015-11-11  
COPY dist/ /dist  
WORKDIR /dist  
RUN tar -xzvf nash-1.0.tar.gz  
WORKDIR /dist/nash-1.0  
RUN python setup.py install  
COPY apa.py /apa/apa.py  
COPY AcquisitionNetwork_PM.py /apa/AcquisitionNetwork_PM.py  
COPY PMTemplateWithOrigin.graphml /apa/PMTemplateWithOrigin.graphml  
WORKDIR /apa  
CMD ["/notebook.sh"]  

