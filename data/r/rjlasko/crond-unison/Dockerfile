FROM rjlasko/minikron:0.5  
MAINTAINER rjlasko  
  
ENV OCAML_VERSION "4.02.2"  
ENV UNISON_VERSION "2.48.3"  
COPY fsroot /  
RUN /bin/sh /tmp/build.sh && \  
rm -rf /tmp/*  

