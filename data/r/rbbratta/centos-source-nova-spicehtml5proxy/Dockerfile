FROM rbbratta/centos-source-nova-base:2.3.20161011  
MAINTAINER Intel Corp. (http://www.intel.com)  
  
  
  
  
  
  
  
RUN mkdir -p /usr/share/nova-spicehtml5proxy-source && git clone
https://github.com/SPICE/spice-html5 /usr/share/nova-spicehtml5proxy-
source/nova-spicehtml5proxy && pushd /usr/share/nova-spicehtml5proxy-
source/nova-spicehtml5proxy && git checkout
54cc41299bea8cd681ed0262735e0fd821cd774a && popd  
  
RUN cd /usr/share \  
&& ln -s nova-spicehtml5proxy-source/* spice-html5  
  
USER nova

