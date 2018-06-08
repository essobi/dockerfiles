FROM openmicroscopy/octave:0.1.0  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
ARG VERSION=5.3.2  
  
USER root  
RUN apt-get update && apt-get install -y wget  
  
USER octave  
RUN wget downloads.openmicroscopy.org/bio-
formats/$VERSION/artifacts/bioformats-octave-$VERSION.tar.gz  
RUN wget downloads.openmicroscopy.org/bio-
formats/$VERSION/artifacts/bioformats_package.jar  
RUN echo "/home/octave/bioformats_package.jar" >>
/home/octave/javaclasspath.txt  
  
  
RUN echo "pkg install bioformats-octave-$VERSION.tar.gz" | octave  

