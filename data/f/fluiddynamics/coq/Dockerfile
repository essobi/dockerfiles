FROM schickling/latex  
RUN apt-get update && apt-get install -y ocaml-nox camlp4 camlp4-extra make  
ADD . ./coq1  
RUN cd coq1 && \  
./configure -prefix /usr/local && \  
make && \  
make install  

