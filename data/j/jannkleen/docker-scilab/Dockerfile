FROM phusion/baseimage:0.9.16  
MAINTAINER jann@resmio.com  
  
# Add external APT repositories  
RUN echo "deb-src http://archive.ubuntu.com/ubuntu vivid main restricted
universe multiverse" | tee /etc/apt/sources.list.d/vivid.list  
  
# Install APT dependencies  
RUN apt-get update -q && apt-get install -q -y build-essential python python-
pip python-dev ca-certificates antlr bwidget tk tk8.6 tcl libtcl8.6 tcl8.6
libtk8.6  
  
# Install vivid version of Scilab  
RUN cd /tmp && apt-get -q -y build-dep libgluegen2-build-java && apt-get -qq
-b source libgluegen2-build-java && dpkg -i libgluegen2-build-java_*_all.deb
&& dpkg -i libgluegen2-jni_*_amd64.deb && dpkg -i libgluegen2-rt-
java_*_all.deb  
RUN cd /tmp && apt-get -q -y build-dep libjogl2-java && apt-get -qq -b source
libjogl2-java && dpkg -i libjogl2-jni_*_amd64.deb && dpkg -i
libjogl2-java_*_all.deb && dpkg -i libjogl2-toolkits_*_all.deb  
RUN cd /tmp && apt-get -q -y build-dep scilab && apt-get -qq -b source scilab
&& dpkg -i scilab-include_*_amd64.deb && dpkg -i scilab-data_*_all.deb && dpkg
-i scilab-minimal-bin_*_amd64.deb && dpkg -i scilab-cli_*_all.deb && dpkg -i
scilab-full-bin_*_amd64.deb && dpkg -i scilab_*_all.deb  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

