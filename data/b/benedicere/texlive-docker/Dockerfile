FROM debian:jessie-slim  
  
RUN apt-get update && \  
apt-get install -y locales rake inkscape texlive texlive-latex-extra texlive-
lang-german gnuplot && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
localedef -i en_US -c -f UTF-8 en_US.UTF-8 && \  
rm -rf /var/cache && \  
rm -rf /var/log  
  
ENV LANG en_US.utf8  

