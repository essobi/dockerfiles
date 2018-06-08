#Pull base image  
FROM rsintegrate/docker-centos-base:7  
MAINTAINER Marshall Nowak <mnowak@integrate.com>  
  
#branch or tag from https://github.com/mono/mono  
ENV MONO_VERSION mono-4.0.1.44  
ENV MONO_PATH=/opt/mono  
ENV PATH=$MONO_PATH/bin:$PATH  
ENV NUGET_PATH /opt/nuget  
ENV NUGET $NUGET_PATH/NuGet.exe  
ENV SCRIPTS_DIR /opt/buildscripts  
  
COPY ./build-mono.sh $SCRIPTS_DIR/build-mono.sh  
COPY ./build-nuget.sh $SCRIPTS_DIR/build-nuget.sh  
RUN chmod -R u+x $SCRIPTS_DIR/*  
RUN /bin/bash -c -e -x ".$SCRIPTS_DIR/build-mono.sh"  
RUN /bin/bash -c -e -x ".$SCRIPTS_DIR/build-nuget.sh"  
  
CMD /bin/bash

