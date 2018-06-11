FROM taccsciapps/base:latest  
  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>  
  
ENV _APP Vina  
ENV _VERSION 1.1.2  
ENV _LICENSE Apache License 2.0  
ENV _AUTHOR "Rion Dooley <dooley@tacc.utexas.edu>, John Fonner
<jfonner@tacc.utexas.edu>"  
WORKDIR /  
  
RUN yum install -y tar time && \  
curl -O http://vina.scripps.edu/download/autodock_vina_1_1_2_linux_x86.tgz &&
\  
tar xzf autodock_vina_1_1_2_linux_x86.tgz && \  
yum erase -y tar && \  
mkdir -p /data  
  
ENV PATH $PATH:/autodock_vina_1_1_2_linux_x86/bin  
  
# Add vina helper script recommended on the project page  
ADD vina_screen_get_top.py /examples/vina_screen_get_top.py  
  
# Adding sci-app usage and doc files  
ADD usage.txt /docs/vina/usage.txt  
ADD intro.txt /docs/vina/intro.txt  
ADD examples.txt /docs/vina/examples.txt  
  
## Adding example data and demo script  
ADD demo.sh /examples/demo.sh  
ADD config.in /examples/config.in  
ADD 1OPK.pdbqt /examples/1OPK.pdbqt  
ADD ZINC00000567.pdbqt /examples/ZINC00000567.pdbqt  
  
# Adding custom invocation and data slicing scripts.  
ADD paramgen.sh /usr/local/bin/paramgen.sh  
ADD vina.sh /usr/local/bin/vina.sh  
  
WORKDIR /data  
  
VOLUME /data  

