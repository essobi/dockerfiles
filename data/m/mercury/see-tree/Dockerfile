FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
tree \  
enscript \  
ghostscript \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV SCRIPTS_LOCATION="/scripts"  
WORKDIR ${SCRIPTS_LOCATION}  
ADD tree-to-pdf.sh ${SCRIPTS_LOCATION}  
  
ENTRYPOINT ["./tree-to-pdf.sh"]  

