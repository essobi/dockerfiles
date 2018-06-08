FROM debian:sid-slim  
MAINTAINER Sylvain Rousseau <thisirs@gmail.com>  
  
# Recreate non-existent directories  
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2 /usr/share/man/man3
/usr/share/man/man4 /usr/share/man/man5 /usr/share/man/man6
/usr/share/man/man7 /usr/share/man/man8  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
texlive-full \  
biber  
  
RUN apt-get install -y --no-install-recommends \  
python-matplotlib \  
python-numpy \  
python-pygments \  
python-scipy \  
python3-matplotlib \  
python3-numpy \  
python3-scipy  
  
RUN apt-get install -y --no-install-recommends \  
r-base \  
r-cran-knitr \  
r-cran-xtable  
  
# epub, html version  
RUN apt-get install -y --no-install-recommends \  
calibre \  
dvipng \  
fonts-liberation \  
imagemagick \  
inkscape \  
ruby \  
scour \  
pandoc \  
tidy \  
python3-html5-parser \  
python3-lxml  
  
RUN apt-get install -y --no-install-recommends \  
plantuml \  
graphviz  
  
RUN apt-get install -y --no-install-recommends \  
git \  
make  
  
# Locale  
RUN apt-get install -y locales  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen  
RUN echo "LC_ALL=fr_FR.UTF-8" >> /etc/profile  
RUN echo "LANG=fr_FR.UTF-8" >> /etc/profile  
RUN echo "export LC_ALL" >> /etc/profile  
RUN echo "export LANG" >> /etc/profile  
  
# Slim down image  
RUN apt-get --purge -y remove tex.\\*-doc$  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

