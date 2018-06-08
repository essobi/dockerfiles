FROM kyokuheki/pandoc  
LABEL maintainer Kyokuheki <kyokuheki@gmail.com>  
  
COPY assets/header.tex /pandoc/header.tex  
COPY assets/template.tex /pandoc/template.tex  
COPY assets/entrypoint.sh /bin/entrypoint.sh  
  
VOLUME ["/src"]  
WORKDIR /src  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  

