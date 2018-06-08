# Using the Ubuntu image  
FROM ubuntu:14.04  
MAINTAINER Ulrich Hoffmann <uh@fh-wedel.de>  
  
# Make sure apt is up to date  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get -qq update && apt-get -qq upgrade  
  
# Not essential, but wise to set the lang  
RUN apt-get -qq install language-pack-en  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Python binary dependencies, developer tools  
RUN apt-get -qq install build-essential make gcc zlib1g-dev git python python-
dev python-pip  
RUN apt-get -qq install libzmq3-dev sqlite3 libsqlite3-dev pandoc
libcurl4-openssl-dev nodejs  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
RUN pip install ipython[notebook]  
RUN pip install numpy  
RUN apt-get -qq install python-scipy  
RUN apt-get -qq install python-matplotlib  
RUN pip install sympy  
RUN pip install simpy  
RUN pip install pandas  
RUN pip install patsy  
RUN pip install scikit-learn  
RUN pip install distribute  
RUN pip install python-dateutil  
RUN pip install statsmodels  
RUN pip install ggplot  
RUN pip install dexy  
RUN pip install watchdog  
RUN pip install pygments  
RUN pip install oct2py  
RUN pip install nltk  
  
WORKDIR /tmp  
RUN git clone git://github.com/pybrain/pybrain.git  
RUN cd pybrain; python setup.py install  
RUN rm -rf /tmp/pybrain  
WORKDIR /notebooks  
  
RUN apt-get -qq install python-opencv  
RUN ln /dev/null /dev/raw1394  
  
EXPOSE 8888  
# run: docker run -d -p 8889:8888 -v /Users/uho/notebooks:/notebooks -e
"PASSWORD=ipython" notebook  
# then connect to https://host:8889/  
# You can mount your own SSL certs as necessary here  
ENV PEM_FILE /key.pem  
ENV PASSWORD Dont make this your default  
  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
  
CMD /notebook.sh  
# run: docker run -d -p 8889:8888 -v /Users/uho/notebooks:/notebooks -e
"PASSWORD=ipython" notebook  

