FROM fedora:latest  
ARG version  
ARG proton  
ENV VERSION=${version:-latest} \  
NAME=service-assurance-poc \  
QPID_PROTON_VERSION=${proton:-0.20.0} \  
PATH=${PATH}:/opt/go/bin  
LABEL maintainer="Tomofumi Hayashi <tohayash@redhat.com>" \  
summary="Docker image for service-assurance-poc." \  
name="s1061123/$NAME" \  
version="$VERSION" \  
version-usage="version: $VERSION (proton: $QPID_PROTON_VERSION)"  
  
COPY ./build.sh /  
RUN ./build.sh  

