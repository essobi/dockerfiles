# MINE container  
# Puts wrapper script 'mine.sh' in path  
# Initial prototype for containerizing, but the gene identifier should conform
to  
# A standardized interface (e.g. https://github.com/bioboxes or
http://nucleotid.es)  
FROM phusion/baseimage  
MAINTAINER Dan Leehr <dan.leehr@duke.edu>  
  
# Install required libraries  
RUN apt-get update && apt-get install -y \  
openjdk-8-jre-headless  
  
# Get MINE  
ENV MINE_DIR /opt/mine  
RUN mkdir -p $MINE_DIR  
  
RUN curl -SL -o $MINE_DIR/MINE.jar http://www.exploredata.net/ftp/MINE.jar  
  
# Copy wrapper script  
COPY mine.sh /usr/bin/mine.sh  
  
# Add to path  
ENV PATH $MINE_DIR:$PATH  
  
CMD ["/usr/bin/mine.sh"]  

