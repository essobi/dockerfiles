FROM debian:9.0  
  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
RUN apt-get install -y make  
  
# full installation is NOT required, though it is ver convenient in real life
;)  
RUN apt-get install -y texlive-full  
  
# none of the following packages is strictly required for all the
presentations.  
# these are needed for particular features, like QR-code generation, C++
sources building, etc...  
RUN apt-get install -y inkscape  
RUN apt-get install -y gnuplot  
RUN apt-get install -y dia  
RUN apt-get install -y graphviz  
RUN apt-get install -y plantuml  
RUN apt-get install -y python-seqdiag  
RUN apt-get install -y qrencode  
RUN apt-get install -y g++  

