# Use the same base image  
FROM python:2  
# for apt-get  
ARG DEBIAN_FRONTEND=noninteractive  
  
# t3basetex: TYPO3 base with tex  
ENV \  
OUR_IMAGE="t3docs/python2-with-latex" \  
OUR_IMAGE_SHORT=t3basetex  
  
# BUILD  
# docker build -t t3docs/python2-with-latex .  
  
LABEL \  
Maintainer="TYPO3 Documentation Team" \  
Description="\  
This is python:2 with LaTeX for TYPO3 \  
Use it as a base image instead of python:2 if you desire LaTeX functionality."
\  
Vendor="t3docs" Version="1.0.0"  
  
RUN \  
true "Create executable COMMENT as a workaround to allow commenting here" \  
&& cp /bin/true /bin/COMMENT \  
\  
&& apt-get update \  
&& COMMENT "Install required packages" \  
&& apt-get install -qy \  
git \  
make \  
\  
&& COMMENT "Install convenience packages" \  
&& apt-get install -qy \  
ncdu \  
rsync \  
\  
&& COMMENT "Install LaTeX" \  
&& COMMENT "see http://www.sphinx-
doc.org/en/stable/builders.html#sphinx.builders.latex.LaTeXBuilder" \  
&& apt-get install -qy texlive-latex-recommended texlive-fonts-recommended
texlive-latex-extra latexmk \  
\  
&& COMMENT "Try extra cleaning besides /etc/apt/apt.conf.d/docker-clean" \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
\  
&& COMMENT "Get TYPO3 latex files" \  
&& git clone https://github.com/TYPO3-Documentation/latex.typo3 \  
/tmp/latex.typo3 \  
\  
&& COMMENT "Run the font installer" \  
&& sh -c "cd /tmp/latex.typo3/font/; ./convert-share-without-sudo.sh" \  
&& rm -rf /tmp/* \  
;  
  
  
WORKDIR /data  
  
VOLUME ["/data"]  

