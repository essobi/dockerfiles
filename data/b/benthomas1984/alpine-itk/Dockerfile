# ITK built in Alpine Linux  
FROM alpine:3.6  
MAINTAINER Benjamin A. Thomas <b.a.thomas@ucl.ac.uk>  
LABEL Description="ITK build" Version="4.12.1"  
RUN apk --update add ca-certificates && apk upgrade  
  
RUN apk add alpine-sdk cmake wget && \  
mkdir -p /opt/ITK-4.12.1/BUILD && cd /opt/ITK-4.12.1 && \  
wget
https://downloads.sourceforge.net/project/itk/itk/4.12/InsightToolkit-4.12.1.tar.gz
&& \  
tar xvzf InsightToolkit-4.12.1.tar.gz && \  
cd /opt/ITK-4.12.1/BUILD && \  
cmake -DBUILD_TESTING:BOOL=OFF -DModule_ITKReview:BOOL=ON
-DCMAKE_BUILD_TYPE:STRING=Release /opt/ITK-4.12.1/InsightToolkit-4.12.1 && \  
make && make install && \  
rm -rf /opt/ITK-4.12.1  
#RUN apk del --purge alpine-sdk cmake wget  

