FROM continuumio/miniconda  
MAINTAINER Fabrice Jossinet (fjossinet@gmail.com)  
RUN apt-get update && apt-get install -y git wget build-essential  
  
#rnaview  
RUN wget -qO RNAVIEW.tar.gz
"https://www.dropbox.com/s/cgbfynqy1vn6ypv/RNAVIEW.tar.gz?dl=0" && tar -xzvf
RNAVIEW.tar.gz  
WORKDIR RNAVIEW/  
RUN make && make clean  
ENV RNAVIEW /RNAVIEW  
  
#Vienna RNA package  
WORKDIR /  
RUN wget -qO ViennaRNA-2.1.8.tar.gz
"https://www.dropbox.com/s/656375q4btupg2x/ViennaRNA-2.1.8.tar.gz?dl=0" && tar
-xzvf ViennaRNA-2.1.8.tar.gz  
WORKDIR ViennaRNA-2.1.8/  
RUN ./configure  
RUN make && make install && make clean  
  
#foldalign  
WORKDIR /  
RUN wget -qO foldalign.2.1.1.tar.gz
"https://www.dropbox.com/s/4ndynu3h806cmmx/foldalign.2.1.1.tar.gz?dl=0" && tar
-xzvf foldalign.2.1.1.tar.gz  
WORKDIR foldalign.2.1.1  
RUN make  
  
#locarna  
WORKDIR /  
RUN wget -qO locarna-1.8.1.tar
"https://www.dropbox.com/s/oo4yg7t41xs8fin/locarna-1.8.1.tar?dl=0" && tar -xvf
locarna-1.8.1.tar  
WORKDIR locarna-1.8.1/  
RUN ./configure --with-vrna=/usr/local/ --without-perl --without-forester
--without-kinfold  
RUN make && make install && make clean  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
WORKDIR /  
  
ENV PATH /RNAVIEW/bin:/foldalign.2.1.1/bin:$PATH  

