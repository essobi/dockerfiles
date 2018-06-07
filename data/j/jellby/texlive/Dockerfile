FROM phusion/baseimage  
  
# Update system and install  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \--no-install-recommends imagemagick poppler-utils && \  
apt-get clean  
  
# Install TexLive  
RUN apt-get install -y \--no-install-recommends wget perl-modules-5.22
libperl5.22 && \  
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \  
mkdir install-tl && \  
tar xvf install-tl-unx.tar.gz -C install-tl \--strip-components=1 && \  
cd install-tl && \  
echo i | ./install-tl && \  
apt-get purge -y \--auto-remove wget perl-modules-5.22 libperl5.22 && \  
cd .. && \  
rm -r install-tl*  
  
# Set up PATH  
RUN export TLPATH=`ls -d /usr/local/texlive/20*/bin/x86_64-linux` && \  
ln -s $TLPATH /texlive  
ENV PATH $PATH:/texlive  

