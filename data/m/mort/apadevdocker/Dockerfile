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
python-xlrd  
  
RUN apt-get -y install python-cvxopt  
RUN apt-get -y --no-install-recommends install python-sympy  
RUN apt-get -y install python-mpmath  
RUN apt-get -y install python-networkx  
RUN pip install jupyter  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
RUN pip install networkx  
  
EXPOSE 8888  
ENV SCRIPTS_CHANGED 2015-12-24  
COPY dist/ /dist  
WORKDIR /dist  
RUN tar -xzvf nash-1.0.tar.gz  
WORKDIR /dist/nash-1.0  
RUN python setup.py install  
WORKDIR /home  
COPY pm.py /home/pm.py  
RUN rm -fr /dist  
CMD ["/notebook.sh"]  

