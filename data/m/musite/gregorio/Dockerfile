FROM debian:unstable  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Mises à jour  
RUN echo deb http://httpredir.debian.org/debian stable main >>
/etc/apt/sources.list; \  
apt-get -y update ; apt-get -y dist-upgrade ; apt-get -y install gnupg2 ; apt-
get -y autoremove --purge; \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
742A4E8A1A1AB4339632CEB3E12CFAE2FE42299E; \  
echo deb http://ppa.launchpad.net/gregorio-project/gregorio/ubuntu xenial main
>> /etc/apt/sources.list; \  
apt-get -y update  
  
# Gestion de l'utf8  
RUN apt-get -y install locales  
RUN locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
ENV LC_ALL C.UTF-8  
# Installation des programmes requis  
RUN apt-get -y --force-yes install --no-install-recommends \  
texlive texlive-latex-recommended texlive-latex-extra texlive-xetex texlive-
luatex \  
texlive-lang-european texlive-lang-french \  
texlive-humanities texlive-extra-utils \  
texlive-fonts-extra fonts-linuxlibertine lmodern texlive-metapost \  
texlive-music gregorio gregoriotex lilypond \  
pandoc  
  
# Contournement temporaire d'un bug de luatex dans la version présente dans
les dépôts  
# et d'un bug dû au mélange de gregorio intégré à TexLive avec la dernière
version.  
# ADD luatex /usr/bin/  
# RUN rm -rf /usr/share/texlive/texmf-dist/tex/lualatex/gregoriotex ; \  
# fmtutil-sys --byfmt=luatex ; fmtutil-sys --byfmt=lualatex ; \  
# fmtutil --byfmt=luatex ; fmtutil --byfmt=lualatex ; \  
# mktexlsr  

