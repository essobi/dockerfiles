FROM ocaml/opam:alpine_ocaml-4.04.0  
RUN sudo -u opam sh -c "cd /home/opam/opam-repository && git pull origin
master" && \  
sudo -u opam sh -c "opam update -u -y" && \  
sudo -u opam sh -c "OPAMYES=1 OPAMJOBS=2 OPAMVERBOSE=1 opam depext -u -i lwt
ssl tls cohttp"  
RUN sudo -u opam sh -c "cd /home/opam/opam-repository && opam-admin make"  
WORKDIR /home/opam/opam-repository  
EXPOSE 8081  
CMD opam config exec \-- cohttp-server-lwt -p 8081  

