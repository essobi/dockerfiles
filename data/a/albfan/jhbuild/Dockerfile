FROM ubuntu:16.10  
LABEL maintainer "waltervargas@linux.com"  
  
ENV USER gnome  
ENV PACKAGES sudo apt-utils apt-file docbook docbook-xsl build-essential git-
core gettext libtext-csv-perl autotools-dev autoconf gettext pkgconf autopoint
yelp-tools  
  
RUN useradd -m -u 1000 $USER  
  
ENV JHBUILD_PATH /home/$USER/jhbuild/checkout  
RUN mkdir -p $JHBUILD_PATH  
ADD . $JHBUILD_PATH/jhbuild  
RUN chown -R $USER /home/$USER  
  
RUN apt-get -y update && \  
apt-get -y install $PACKAGES && \  
apt-file update && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/nopasswd  
  
USER $USER  
WORKDIR $JHBUILD_PATH/jhbuild  
  
RUN ./autogen.sh --simple-install  
RUN make  
RUN make install  
  
RUN echo 'PATH=~/.local/bin:$PATH' >> $HOME/.bashrc  
ENV PATH $HOME/.local/bin:$PATH  

