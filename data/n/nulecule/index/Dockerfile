FROM vpavlin/atomicapp  
  
LABEL RUN="docker run --rm $IMAGE"  
  
RUN cd /tmp && \  
atomicapp index generate https://github.com/projectatomic/nulecule-library &&
\  
mv gen_index.yaml /gen_index.yaml  
  
ENTRYPOINT echo "This image contains index information about Nulecule
applications stored in nulecule-library"  

