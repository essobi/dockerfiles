FROM debian:testing  
  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula \  
select true | debconf-set-selections  
  
RUN echo "deb http://deb.debian.org/debian testing contrib" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
make \  
texlive-full \  
ttf-mscorefonts-installer && \  
# Removing documentation packages *after* installing them is kind of hacky,  
# but it only adds some overhead while building the image.  
apt-get \--purge remove -y .\\*-doc$ && \  
# Remove more unnecessary stuff  
apt-get clean -y  
  

