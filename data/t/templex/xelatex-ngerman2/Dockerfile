#: title : templex/xelatex-ngerman2  
#: author : "Fabian Tolkmitt" <ftolkmitt@gmail.com>  
#: version: "1.0.0"  
# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:latest  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
COPY . /my_files  
  
# ...put your own build instructions here...  
# Install all TeX and LaTeX dependences  
RUN apt-get update && \  
apt-get install --yes \--no-install-recommends \  
fontconfig \  
git \  
ca-certificates \  
inotify-tools \  
lmodern \  
make \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-lang-english \  
texlive-lang-portuguese \  
texlive-xetex \  
texlive-fonts-extra \  
texlive-lang-german \  
pandoc && \  
apt-get autoclean && apt-get --purge --yes autoremove && \  
cp -R /my_files/fonts/* /usr/share/fonts && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

