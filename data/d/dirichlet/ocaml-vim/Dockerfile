FROM dirichlet/basic-vim  
  
RUN echo "deb http://ppa.launchpad.net/avsm/ocaml42+opam12/ubuntu trusty main"
| tee -a /etc/apt/sources.list  
  
RUN echo "deb-src http://ppa.launchpad.net/avsm/ocaml42+opam12/ubuntu trusty
main" | tee -a /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --force-yes ocaml ocaml-native-
compilers camlp4-extra opam  
  
RUN apt-get clean && apt-get update && apt-get install -y make  
  
RUN opam init  
  
RUN apt-get install -y m4  
  
RUN printf 'Y' | opam install menhir ounit utop  

