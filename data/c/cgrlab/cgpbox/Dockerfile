FROM quay.io/wtsicgp/cgp_in_a_box:latest  
  
MAINTAINER keiranmraine@gmail.com  
  
ENV CGPBOX_VERSION 2.0.0  
  
LABEL uk.ac.sanger.cgp="Cancer Genome Project, Wellcome Trust Sanger
Institute" \  
version="$CGPBOX_VERSION" \  
description="The CGP somatic calling pipeline 'in-a-box'"  
  
USER  root  
  
ENV OPT /opt/wtsi-cgp  
ENV PATH $OPT/bin:$PATH  
ENV PERL5LIB $OPT/lib/perl5  
  
RUN apt-get -yq update && apt-get -yq install xvfb && apt-get -yq install
libpango1.0-dev  
  
RUN echo "options(bitmapType='cairo')" > ~/.Rprofile  
  
ENTRYPOINT []  
CMD ls -lhrt  

