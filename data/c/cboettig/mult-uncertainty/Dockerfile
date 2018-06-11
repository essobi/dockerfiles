FROM ubuntu:15.04  
RUN apt-get update && apt-get -y install epstool fig2ps less git octave
octave-statistics vim  
COPY run.sh /usr/bin/local/run  
CMD ["/bin/bash", "-e", "/usr/bin/local/run"]  

