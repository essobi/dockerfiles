FROM brimstone/ubuntu:14.04  
LABEL FUNCTION_NAME panreveal  
  
RUN package pandoc ca-certificates  
  
WORKDIR /  
  
ADD reveal.js /reveal.js  
  
ADD default.revealjs /usr/share/pandoc/data/templates/default.revealjs  
  
ENTRYPOINT ["/usr/bin/pandoc", "-f", "markdown_github", "-t", "revealjs", "--
self-contained"]  
  
CMD []  

