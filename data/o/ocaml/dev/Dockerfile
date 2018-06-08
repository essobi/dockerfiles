FROM ocaml/opam:ubuntu-16.04_ocaml-4.03.0  
RUN sudo -u opam sh -c "opam depext -u conf-vim conf-emacs merlin annot utop
tuareg lwt jenga" && \  
sudo -u opam sh -c "opam install -y -j 2 -v conf-vim conf-emacs merlin annot
utop tuareg lwt jenga"

