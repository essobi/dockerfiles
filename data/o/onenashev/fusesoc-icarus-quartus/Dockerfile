# The MIT License  
#  
# Copyright (c) 2016, Oleg Nenashev  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in  
# all copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
# THE SOFTWARE.  
FROM cdsteinkuehler/jessie-quartus-15.1.2:latest  
MAINTAINER Oleg Nenashev <o.v.nenashev@gmail.com>  
LABEL Description="The image offers FuseSoC, Icarus Verilog and Quartus
15.1.2" Vendor="Oleg Nenashev" Version="0.1"  
  
# Parameters  
ARG ZLIB_VERSION=1.2.8  
ARG ICARUS_VERILOG_VERSION=10_1  
ARG FUSESOC_VERSION=1.5  
USER root  
  
RUN apt-get update  
RUN apt-get install -y python2.7-dev libyaml-dev libyaml-dev  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-yaml  
RUN apt-get install -y git  
  
# Install ZLIB for Icarus  
RUN apt-get install -y wget build-essential  
WORKDIR /zlib  
RUN wget http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz && tar zxf
zlib-${ZLIB_VERSION}.tar.gz  
WORKDIR /zlib/zlib-${ZLIB_VERSION}  
RUN ./configure && make  
RUN make install  
  
# Install Icarus Verilog  
RUN apt-get install -y libelf-dev autoconf gperf bison flex  
RUN git clone https://github.com/steveicarus/iverilog.git  
WORKDIR iverilog  
RUN git checkout v${ICARUS_VERILOG_VERSION}  
RUN sh autoconf.sh  
RUN ./configure  
RUN make  
RUN make install  
  
#TODO: Fix Java  
# Install Java (required for using the image as Jenkins slave/agent)  
# run apt-get install -y software-properties-common  
# RUN add-apt-repository ppa:openjdk-r/ppa  
# RUN apt-get update  
# RUN apt-get install -y openjdk-8-jre  
# RUN update-alternatives --config java  
# RUN update-alternatives --config javac  
# Install FuseSoC  
ENV FUSESOC_VERSION=${FUSESOC_VERSION}  
  
WORKDIR /var/lib/fusesoc  
RUN git clone https://github.com/olofk/fusesoc.git  
RUN mv /var/lib/fusesoc/fusesoc /var/lib/fusesoc/repo  
WORKDIR /var/lib/fusesoc/repo  
RUN git checkout ${FUSESOC_VERSION}  
  
#For the local run: COPY fusesoc /var/lib/fusesoc  
RUN python setup.py install  
  
# Prepare run home  
RUN mkdir /fusesoc  
RUN chmod -R 777 /fusesoc  
ENV HOME /fusesoc  
#TODO: Allow specifying a configurable log destination  
#ENV FUSESOC_LOG /fusesoc/fusesoc.log  
RUN touch /var/lib/fusesoc/repo/fusesoc.log  
RUN chmod 777 /var/lib/fusesoc/repo/fusesoc.log  
COPY fusesoc.conf /etc/fusesoc/fusesoc.conf  
  
# Install Cyclone IV packages (they are kept wihout "iv" suffix for this
release)  
#ADD
http://download.altera.com/akdlm/software/acdsinst/15.1/185/ib_installers/cyclone-15.1.0.185.qdz
/tmp/  
#ADD
http://download.altera.com/akdlm/software/acdsinst/15.1/185/ib_installers/QuartusLiteSetup-15.1.0.185-linux.run
/tmp/  
# Fix file permissions  
#RUN cd /tmp/ && \  
# chmod +x *.run && \  
# chmod +r *  
#USER builder  
#RUN cd /tmp/ && \  
# ./QuartusLiteSetup-15.1.0.185-linux.run --mode unattended  
#USER root  
# Initialization will be done for the user on startup  
COPY fusesoc-entrypoint.sh /usr/local/bin/fusesoc-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/fusesoc-entrypoint.sh"]  
CMD ["fusesoc"]

