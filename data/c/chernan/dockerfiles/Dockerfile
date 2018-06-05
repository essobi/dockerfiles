### SamTools version 0.1.19  
#  
# Build image  
#  
# docker build -t samtools:0.1.19 .  
#  
# Run samtools through the image  
#  
# (assuming that you followed instructions here:
https://github.com/boot2docker/boot2docker#folder-sharing  
# and that you copied a file named `my_test_file.bam` in your shared partition
(/Volumes/data on host).)  
#  
# docker run -it --volumes-from my-data samtools:0.1.19 samtools index
/data/my_test_file.bam  
#  
#  
#  
################################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Celine HERNANDEZ <chernand@biologie.ens.fr>  
  
################################################################  
  
# Update the repository sources list and upgrade packages  
RUN apt-get update  
RUN apt-get -qq --assume-yes upgrade  
  
# Install cURL to download samtools  
RUN apt-get --assume-yes install curl  
# Tools to compile  
RUN apt-get --assume-yes install gcc make  
# Additional libraries needed for compilation (more specifically: zlib.h and
curses.h)  
RUN apt-get --assume-yes install zlib1g-dev libncurses5-dev  
  
# Download SamTools using cURL  
# NB: option -L follows redirections  
RUN curl
http://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download
-o /tmp/samtools-0.1.19.tar.bz2 -L  
  
# Install SamTools  
RUN mkdir /usr/local/samtools  
RUN tar -xjf /tmp/samtools-0.1.19.tar.bz2 -C /usr/local/samtools  
RUN chmod 755 /usr/local/samtools/samtools-0.1.19  
RUN cd /usr/local/samtools/samtools-0.1.19/ ; make  
RUN ln -s /usr/local/samtools/samtools-0.1.19/samtools /usr/local/bin/samtools  
ENV PATH /usr/local/bin/samtools:$PATH  
  
# Cleanup  
RUN rm -rf /tmp/samtools*  
  
# Execute at start up  
CMD samtools  
  
###############################################################  

