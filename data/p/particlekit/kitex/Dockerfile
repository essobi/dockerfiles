FROM opensuse:leap  
  
  
RUN zypper --non-interactive in \--auto-agree-with-licenses --no-recommends \  
make unzip texlive-collection-bibtexextra texlive-collection-latexextra \  
texlive-collection-pstricks texlive-collection-publishers \  
texlive-collection-science texlive-inconsolata texlive-metapost \  
texlive-tools texlive-sourcesanspro texlive-newtx texlive-libertine \  
linux-libertine-fonts texlive-boondox fetchmsttfonts patterns-openSUSE-fonts \  
texlive-babel-german texlive-bbm texlive-helvetic-fonts texlive-helvetic\  
texlive-latexmk texlive-latexmk-bin &&\  
zypper clean --all  
  
ADD getnonfreefonts-sys /usr/local/bin/  
ADD tex /usr/share/texmf/tex  
  
RUN export TEXMFLOCAL=/usr/share/texmf/ && export TEXMFHOME=/usr/share/texmf/
&&\  
chmod 755 /usr/local/bin/getnonfreefonts-sys &&\  
chgrp -R mktex /usr/share/texmf/ &&\  
/usr/local/bin/getnonfreefonts-sys -a &&\  
echo y | /usr/bin/updmap-sys --syncwithtrees --outputdir /usr/share/texmf/ &&\  
/usr/local/bin/getnonfreefonts-sys -r &&\  
mkdir /cache  
  
WORKDIR /cache  
VOLUME ["/cache"]  
  

