FROM debian:jessie  
  
RUN apt-get update && apt-get install -y pandoc latex-beamer texlive-fonts-
recommended  
  
ENTRYPOINT ["/usr/bin/pandoc","-t","beamer"]  

