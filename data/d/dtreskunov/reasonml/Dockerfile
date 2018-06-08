#dtreskunov/reasonml:local  
FROM ocaml/opam:alpine_ocaml-4.06.0_flambda  
  
ENV OPAMYES=true  
  
RUN sudo apk update  
RUN sudo apk add m4  
WORKDIR /home/opam/opam-repository  
RUN git pull --quiet  
RUN opam update  
RUN opam upgrade  
  
# Template project  
COPY template-project /template-project  
RUN sudo chown -R opam:nogroup /template-project  
RUN opam pin add template-project /template-project --no-action  
RUN opam depext --install template-project  
  
# Emacs goodies  
WORKDIR /home/opam  
RUN sudo apk add diffutils the_silver_searcher emacs-gtk2  
RUN opam install merlin  
RUN opam install ocp-indent  
RUN opam install user-setup  
RUN opam install tuareg  
COPY .emacs.d .emacs.d  
RUN sudo chown -R opam:nogroup .emacs.d  
RUN mkdir -p .emacs.d/vendor && \  
cd .emacs.d/vendor && \  
git clone \--quiet https://github.com/Khady/merlin-eldoc.git  
RUN opam user-setup install  
RUN emacs --script .emacs.d/init.el  
  
# Install Source Code Pro font  
RUN sudo git clone \--depth 1 --branch release https://github.com/adobe-
fonts/source-code-pro.git /usr/share/fonts/source-code-pro && \  
sudo fc-cache -f -v  
  
WORKDIR /template-project  
ENV OPAMYES=  

