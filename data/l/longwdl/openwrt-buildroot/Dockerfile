FROM ubuntu:12.04  
# Run updates  
RUN apt-get update -qq  
  
# Add sudo user owrt  
RUN apt-get install -y sudo  
RUN useradd -m owrt  
RUN echo 'owrt ALL=NOPASSWD: ALL' > /etc/sudoers.d/owrt  
  
# Prepare dependency  
RUN apt-get install -y subversion flex sharutils curl \  
build-essential libpq-dev build-essential ccache \  
libncurses5-dev zlib1g-dev xsltproc git gengetopt \  
gettext libssl-dev libxml-parser-perl gawk file \  
python unzip wget default-jre-headless ocaml-nox \  
vim pkg-config  
  
RUN apt-get clean  
  
# Change user  
USER owrt  

