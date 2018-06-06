FROM ubuntu:14.04.2  
MAINTAINER frederic.osterrath@crim.ca  
  
RUN apt-get update && apt-get install -y \  
curl \  
libqt5network5 \  
libqt5xml5  
  
# This installs the annotation program.  
RUN curl https://code.soundsoftware.ac.uk/attachments/download/1619/sonic-
annotator-linux64-1.2.tar.bz2 > /tmp/sonic-annotator-linux64.tar.bz2 && \  
cd /tmp && \  
tar xjvf sonic-annotator-linux64.tar.bz2 && \  
mv sonic-annotator/sonic-annotator /usr/local/bin && \  
rm -rf sonic-annotator sonic-annotator-linux64.tar.bz2  
  
# This installs the plug-in which is used by the annotation program.  
RUN mkdir ~/vamp && \  
cd ~/vamp && \  
curl https://code.soundsoftware.ac.uk/attachments/download/1591/silvet-
linux64-v1.1.tar.bz2 > silvet.tar.bz2 && \  
tar xjvf silvet.tar.bz2 && \  
mv silvet-linux64-v1.1/silvet* . && \  
rm -rf silvet-linux64-v1.1 silvet.tar.bz2  
  
COPY transform.ttl /etc/transform.ttl  
  
ENTRYPOINT ["/usr/local/bin/sonic-annotator"]  

