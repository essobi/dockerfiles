FROM ubuntu:14.04  
MAINTAINER Shingo Sato <shinsugar@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y make automake g++  
RUN apt-get install -y libpoppler-glib-dev poppler-utils wxgtk3.0-dev  
RUN apt-get install -y git  
  
WORKDIR /app  
RUN git clone \--depth=1 https://github.com/vslavik/diff-pdf.git .  
  
RUN ./bootstrap  
RUN ./configure  
RUN make  
RUN make install  

