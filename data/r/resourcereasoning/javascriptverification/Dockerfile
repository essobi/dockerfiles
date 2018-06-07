# Dockerfile to produce a container containing the required build environment  
FROM ocaml/opam:ubuntu-16.04_ocaml-4.05.0  
USER root  
RUN apt-get update && apt-get install -y \  
libz3-dev \  
nodejs \  
nodejs-legacy \  
python \  
python-psycopg2 \  
virtualenv \  
z3  
USER opam  

