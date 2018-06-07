FROM ubuntu:zesty  
  
RUN apt-get -y update  
RUN apt-get -y install nginx webhook  
RUN apt-get -y install git make wget  
RUN apt-get -y install rsync python python-watchdog  
RUN apt-get -y install python3 python3-pandocfilters pandoc texlive-latex-
extra  
  
COPY ext /ext  
  
CMD /ext/bin/cucyber-init  
  
EXPOSE 8000  

