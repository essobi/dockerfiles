FROM ubuntu:15.04  
MAINTAINER ryoheisonoda@outlook.com  
  
RUN apt-get install -y curl && \  
curl -L https://www.ubuntulinux.jp/ubuntu-ja-archive-keyring.gpg | apt-key add
\- && \  
curl -L https://www.ubuntulinux.jp/ubuntu-jp-ppa-keyring.gpg | apt-key add \-
&& \  
curl -L https://www.ubuntulinux.jp/sources.list.d/vivid.list >
/etc/apt/sources.list.d/ubuntu-ja.list  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk graphviz python-pip python-dev build-
essential zlib1g-dev \  
fonts-ipafont-gothic fonts-ipafont-mincho fonts-takao-pgothic fonts-takao-
gothic \  
fonts-takao-mincho texlive texlive-lang-cjk libjpeg8 libjpeg8-dev \  
libfreetype6 libfreetype6-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Sphinx, sphinxcontrib-*  
RUN pip install Sphinx sphinxcontrib-plantuml sphinxcontrib-blockdiag
sphinxcontrib-seqdiag  
# Download PlantUML  
RUN curl -L
http://sourceforge.net/projects/plantuml/files/plantuml.jar/download >
/plantuml.jar  
  
ADD build /build  
CMD /bin/bash /build  

