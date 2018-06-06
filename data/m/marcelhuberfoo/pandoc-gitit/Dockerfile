FROM marcelhuberfoo/cabal-build  
  
MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>  
  
USER root  
RUN echo -e '[infinality-bundle]\nSigLevel=Never\nServer =
http://bohoomil.com/repo/$arch\n[infinality-bundle-
fonts]\nSigLevel=Never\nServer = http://bohoomil.com/repo/fonts' >>
/etc/pacman.conf && \  
pacman -Syy \--noconfirm reflector git && \  
reflector \--latest 10 \--sort rate \--save /etc/pacman.d/mirrorlist && \  
pacman -Syyu \--noconfirm && printf "y\\\ny\\\n" | pacman -Scc  
  
USER $UNAME  
RUN bash -l -c 'cabal update && git clone https://github.com/jgm/gitit && cd
gitit && \  
cabal install \--jobs \--allow-newer \--enable-executable-stripping \--enable-
split-objs \--flags="embed_data_files plugins" \--disable-executable-dynamic
\--disable-debug-info \--disable-tests \--disable-documentation
\--dependencies-only . pandoc pandoc-citeproc && cabal install hsb2hs && \  
cabal install \--jobs \--allow-newer \--enable-executable-stripping \--enable-
split-objs \--flags="embed_data_files plugins" \--disable-executable-dynamic
\--disable-debug-info \--disable-tests \--disable-documentation . pandoc
pandoc-citeproc && \  
cd && rm -rf gitit/ .cabal/{logs,packages,setup-exe-cache}/*'  
  
USER root  
RUN reflector \--latest 10 \--sort rate \--save /etc/pacman.d/mirrorlist  
RUN pacman -Syy \--noconfirm \--needed fontconfig-infinality-ultimate
freetype2-infinality-ultimate cairo-infinality-ultimate ibfonts-meta-base &&
printf "y\\\ny\\\n" | pacman -Scc  
RUN pacman -S \--noconfirm \--needed python-pip texlive-latexextra inkscape
gtk2 graphviz mime-types jre8-openjdk-headless pkg-config && \  
printf "y\\\ny\\\n" | pacman -Scc  
RUN pip install pandocfilters pygraphviz  
  
RUN cd / && git clone \--single-branch \--branch master \--depth 1
https://github.com/marcelhuberfoo/pandocfilters.git filters  
RUN chmod -R 0755 /filters  
COPY plantuml /usr/local/bin/plantuml  
RUN mkdir -p /opt/plantuml && curl -L -o /opt/plantuml/plantuml.jar
http://sourceforge.net/projects/plantuml/files/plantuml.jar/download && chmod
+x /usr/local/bin/plantuml  
  
ADD entrypoint.sh /entrypoint.sh  
RUN rm -f /tmp/* || true  
EXPOSE 5001  
#CMD ["gitit", "-f", "/data/gitit.conf"]  
CMD ["pandoc", "--help"]  
  

