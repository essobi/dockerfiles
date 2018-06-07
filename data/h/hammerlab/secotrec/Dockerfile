FROM hammerlab/coclobas  
# to get opam, gcloud, & more  
# We want everything cutting edge  
RUN sudo apt-get update  
RUN sudo apt-get upgrade --yes  
  
RUN opam remote add mothership https://opam.ocaml.org  
RUN opam remote remove default  
RUN opam update  
RUN opam upgrade --yes  
  
# The current installation procedure for Secotrec:  
RUN opam pin -n add coclobas https://github.com/hammerlab/coclobas.git  
RUN opam pin -n add ketrew https://github.com/hammerlab/ketrew.git  
RUN opam pin -n add biokepi https://github.com/hammerlab/biokepi.git  
RUN opam pin -n add genspio https://github.com/hammerlab/genspio.git  
RUN opam pin -n add secotrec https://github.com/hammerlab/secotrec.git  
RUN opam upgrade  
RUN opam install tls secotrec biokepi  
  
# This is needed for the DNS check happening as part of `secotrec-gke up`:  
RUN sudo apt-get install -y dnsutils  

