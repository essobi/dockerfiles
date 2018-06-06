FROM bitnami/minideb-extras:jessie-r13  
  
MAINTAINER Bitnami <containers@bitnami.com>  
  
RUN install_packages git build-essential pkg-config cmake clang ninja-build
libncurses5-dev automake m4 groff gperf zip file \  
rsync libtool unzip libltdl7- # libltdl makes upstream imap link with it but
with missing symbols  
ENTRYPOINT [] # Disable entrypoint from Stacksmith  

