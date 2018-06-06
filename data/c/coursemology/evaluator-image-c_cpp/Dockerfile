FROM coursemology/evaluator-image-base:latest  
MAINTAINER Coursemology <coursemology@googlegroups.com>  
  
# Set HOME variable to a location accessible by the coursemology user  
# Needed to clone GoogleTest framework to a location accessible by the
coursemology user.  
ENV HOME /home/coursemology  
  
RUN apt-get update && apt-get install -y --force-yes \  
build-essential git \  
&& git clone https://github.com/google/googletest.git $HOME/googletest \  
&& apt-get remove -y git \  
&& apt-get autoremove -y \  
&& apt-get install -y wget \  
&& cd $HOME/ \  
&& mkdir boost \  
&& cd boost \  
&& wget
https://sourceforge.net/projects/boost/files/boost/1.64.0/boost_1_64_0.tar.gz/download
\  
&& tar xvfz download \  
&& rm download \  
&& cd boost_1_64_0/ \  
&& ./bootstrap.sh \  
&& ./b2 stage threading=multi link=static \  
&& ./b2 install threading=multi link=static \  
&& cd ../../ \  
&& rm -Rf boost/ \  
&& apt-get remove -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV BOOST_DIR /usr/local/lib  
# Compile GTest library so that it doesn't need to be compiled on each
evaluation  
# The GTEST library would then be available as ${GTEST_DIR}/libgtest.a  
ENV GTEST_DIR $HOME/googletest/googletest  
  
RUN cd $GTEST_DIR/ \  
&& g++ -isystem ${GTEST_DIR}/include -I${GTEST_DIR} \  
-pthread -c ${GTEST_DIR}/src/gtest-all.cc \  
&& ar -rv libgtest.a gtest-all.o  
  
# Set env var for GoogleTest to output an xml report file  
ENV GTEST_OUTPUT xml:./report.xml  

