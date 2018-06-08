FROM sharelatex/sharelatex  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN add-apt-repository ppa:gregorio-project/gregorio ; apt-get update ; \  
apt-get -y --force-yes install --no-install-recommends \  
fonts-linuxlibertine lmodern gregorio  
  
RUN tlmgr update --self ; \  
tlmgr install collection-music collection-humanities \  
collection-latexrecommended collection-luatex \  
collection-fontsrecommended libertine \  
collection-langfrench collection-langeuropean \  
xkeyval keycommand xstring environ trimspaces currfile ; \  
ln -s \  
/usr/local/texlive/2017/texmf-dist/scripts/lyluatex/lyluatex.lua \  
/usr/local/texlive/2017/texmf-dist/tex/latex/lyluatex/ ; \  
mktexlsr  
  
RUN wget \  
'http://download.linuxaudio.org/lilypond/binaries/linux-64/'$(wget \  
'http://download.linuxaudio.org/lilypond/binaries/linux-64/' \  
-O- 2>&1 | grep -oh '"lilypond.*.sh"' | tail -1 | sed s/\"//g) ; \  
sh ./lilypond*.sh --batch ; \  
rm ./lilypond*.sh  
  
# RUN apt-get -y --force-yes install --no-install-recommends lilypond  
RUN sed -i s/'"-interaction=batchmode"'/'"-interaction=batchmode", "-shell-
escape"'/ \  
/var/www/sharelatex/clsi/app/js/LatexRunner.js  
  
EXPOSE 80  
WORKDIR /  
  
ENTRYPOINT ["/sbin/my_init"]  

