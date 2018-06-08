FROM pataquets/docker-nerdshow  
  
ONBUILD COPY . /presentation/  
ONBUILD RUN nerdshow-generate /presentation/presentation.json --zoom-enabled  
  
ENTRYPOINT [ "nerdshow", "/presentation/" ]  

