# Glimmer container  
# Puts Glimmer 'glimmer3' and other binaries in path.  
# Initial prototype for containerizing, but the gene identifier should conform
to  
# A standardized interface (e.g. https://github.com/bioboxes or
http://nucleotid.es)  
FROM phusion/baseimage  
MAINTAINER Dan Leehr <dan.leehr@duke.edu>  
  
# Install required libraries  
RUN apt-get update && apt-get install -y \  
build-essential \  
csh \  
python  
  
# Get Glimmer  
ENV GLIMMER_VERSION 302b  
ENV GLIMMER_DIR /opt/glimmer  
# The archive extracts a subdirectory  
ENV GLIMMER_SUBDIR glimmer3.02  
RUN mkdir -p $GLIMMER_DIR  
  
# Save version to a file  
RUN echo $GLIMMER_VERSION > $GLIMMER_DIR/VERSION  
  
# This extracts a directory called 'glimmer3.02'  
RUN curl -SL
https://ccb.jhu.edu/software/glimmer/glimmer$GLIMMER_VERSION.tar.gz | tar -xzC
$GLIMMER_DIR  
RUN cd $GLIMMER_DIR/$GLIMMER_SUBDIR/src && make  
  
# Update paths in the g3-iterated.csh script  
# set awkpath = /fs/szgenefinding/Glimmer3/scripts  
# set glimmerpath = /fs/szgenefinding/Glimmer3/bin  
# set elphbin = /nfshomes/adelcher/bin/elph  
# Add glimmer to path  
ENV PATH
$GLIMMER_DIR/$GLIMMER_SUBDIR/bin:$GLIMMER_DIR/$GLIMMER_SUBDIR/scripts:$PATH  
  
# Get ELPH - from https://ccb.jhu.edu/software/ELPH/  
ENV ELPH_VERSION 1.0.1  
ENV ELPH_DIR /opt/ELPH  
RUN mkdir -p $ELPH_DIR  
# This extracts a directory called ELPH  
RUN curl -SL
ftp://ftp.cbcb.umd.edu/pub/software/elph/ELPH-$ELPH_VERSION.tar.gz | tar -xzC
$ELPH_DIR  
# ELPH compiles locally  
RUN cd $ELPH_DIR/ELPH/sources && make  
  
# Place elph binary and add to path  
RUN mkdir -p $ELPH_DIR/bin  
RUN mv $ELPH_DIR/ELPH/sources/elph $ELPH_DIR/bin/elph  
ENV PATH $ELPH_DIR/bin:$PATH  
  
# Update hard-coded paths in g3-iterated.csh  
RUN sed -i "s|/fs/szgenefinding/Glimmer3|${GLIMMER_DIR}/${GLIMMER_SUBDIR}|g"
$GLIMMER_DIR/$GLIMMER_SUBDIR/scripts/g3-iterated.csh  
RUN sed -i "s|/nfshomes/adelcher/bin/elph|${ELPH_DIR}/bin/elph|g"
$GLIMMER_DIR/$GLIMMER_SUBDIR/scripts/g3-iterated.csh  
  
# Update awk paths in awk scripts  
RUN sed -i "s|/bin/awk|/usr/bin/awk|g"
$GLIMMER_DIR/$GLIMMER_SUBDIR/scripts/*.awk  
  
# Python script is used to number lines in the fasta file  
COPY number_orfs.py /usr/bin/number_orfs.py  
  
# Place wrapper script  
COPY glimmer.sh /usr/bin/glimmer.sh  
  
CMD ["/usr/bin/glimmer.sh"]  

