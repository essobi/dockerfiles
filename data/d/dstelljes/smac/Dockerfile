FROM fedora:24  
MAINTAINER Dan Stelljes <stell124@morris.umn.edu>  
  
RUN dnf install -y java-1.8.0-openjdk-headless tar  
  
WORKDIR /  
ADD
http://www.cs.ubc.ca/labs/beta/Projects/SMAC/smac-v2.10.03-master-778.tar.gz
./  
RUN tar -zxf smac*.tar.gz  
RUN rm -f smac*.tar.gz  
RUN mv smac* smac-2.10  
RUN sed -i -r 's/^(DIR="\$\\( .*)$/DIR=`realpath $0`/' smac-2.10/smac  
RUN ln -s /smac-2.10/smac /usr/bin/smac  
  
RUN dnf remove -y tar  
RUN dnf clean all  

