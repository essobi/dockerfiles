FROM ubuntu:16.04  
MAINTAINER Johan Pauwels <http://www.eecs.qmul.ac.uk/people/view/50775/johan-
pauwels>  
RUN apt-get update && apt-get install -y \  
build-essential \  
libbz2-dev \  
libfftw3-dev \  
libfishsound1-dev \  
libid3tag0-dev \  
liblo-dev \  
liblrdf0-dev \  
libmad0-dev \  
liboggz2-dev \  
libpulse-dev \  
libsamplerate-dev \  
libsndfile-dev \  
libsord-dev \  
libxml2-utils \  
portaudio19-dev \  
qt5-default \  
raptor-utils \  
vamp-examples \  
vamp-plugin-sdk \  
yajl-tools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Compile sonic-annotator  
ADD https://code.soundsoftware.ac.uk/attachments/download/1867/sonic-
annotator-1.4.tar.gz .  
RUN tar xzf sonic-annotator-1.4.tar.gz && rm sonic-annotator-1.4.tar.gz  
WORKDIR sonic-annotator-1.4  
### Compile Vamp SDK  
WORKDIR vamp-plugin-sdk  
RUN ./configure && make install && make clean  
WORKDIR ..  
### Compile Vamp test plugin (prerequisite for sonic-annotator tests)  
ADD https://code.soundsoftware.ac.uk/attachments/download/1583/vamp-test-
plugin-1.1.tar.gz .  
RUN tar xzf vamp-test-plugin-1.1.tar.gz && rm vamp-test-plugin-1.1.tar.gz  
WORKDIR vamp-test-plugin-1.1  
RUN make -f Makefile.linux && mv vamp-test-plugin.* /usr/lib/vamp/ && make -f
Makefile.linux clean  
WORKDIR ..  
RUN rm -rf vamp-test-plugin-1.1  
### Compile sonic-annotator itself  
RUN ./configure && (make || true) && make clean  
WORKDIR ..  
  
# Compile VamPy  
RUN apt-get update && apt-get install -y \  
libpython-dev \  
python-numpy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
ADD http://code.soundsoftware.ac.uk/attachments/download/672/vampy-2.0.tar.bz2
.  
RUN tar xjf vampy-2.0.tar.bz2 && rm vampy-2.0.tar.bz2  
WORKDIR vampy-2.0  
RUN sed -i 's/python2.6/python2.7/g' Makefile.linux  
RUN make -f Makefile.linux && make -f Makefile.linux install && make -f
Makefile.linux clean  
WORKDIR ..  

