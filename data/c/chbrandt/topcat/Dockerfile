FROM ubuntu  
  
LABEL Description=TOPCAT\ is\ an\ interactive\ graphical\ viewer\ and\ editor\
for\ astronomical\ tabular\ data.\  
Author=Mark\ Taylor\  
URL=http://www.star.bris.ac.uk/~mbt/topcat  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y default-jre && \  
apt-get install -y wget git-core && \  
apt-get clean  
  
RUN wget -q -O /topcat.jar http://www.star.bris.ac.uk/~mbt/topcat/topcat-
full.jar  
  
RUN git clone https://github.com/chbrandt/docker_commons.git && \  
ln -sf docker_commons/entrypoint.sh /.  
  
ENV EXECAPP java  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["-jar /topcat.jar"]  

