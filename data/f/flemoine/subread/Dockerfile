FROM ubuntu  
  
MAINTAINER Frederic Lemoine  
  
#  
# Install pre-requistes  
#  
RUN apt-get update --fix-missing  
RUN apt-get install -q -y wget g++ gcc make zlib1g-dev  
  
RUN \  
wget
"http://downloads.sourceforge.net/project/subread/subread-1.5.0-p2/subread-1.5.0-p2-source.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubread%2Ffiles%2Fsubread-1.5.0-p2%2F&ts=1461157751&use_mirror=iweb"
&& \  
mv subread* subread-1.5.0-p2-source.tar.gz && \  
tar -xzvf subread-1.5.0-p2-source.tar.gz && \  
cd subread-1.5.0-p2-source/src && \  
make -f Makefile.Linux && \  
mkdir /opt/subread/ && \  
cp -r ../bin/* /opt/subread && \  
cd ../ && \  
rm -rf subread-1.5.0-p2-source/ subread-1.5.0-p2-source.tar.gz  
  
RUN apt-get remove -q -y zlib1g-dev wget g++ gcc make \  
&& apt-get autoremove -y  
  
ENV PATH
/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/subread/  

