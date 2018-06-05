# Kallisto  
# VERSION 0.42.3  
#### # Kallisto - kallisto is a program for quantifying abundances of
transcripts from RNA-Seq data # Nicolas L Bray, Harold Pimentel, Páll Melsted
and Lior Pachter, Near-optimal probabilistic RNA-seq quantification # Nature
Biotechnology 34, 525–527 (2016), doi:10.1038/nbt.3519 ####  
#  
FROM ubuntu:14.04.3  
MAINTAINER Kapeel Chougule  
  
LABEL Description="This image is used for running Kallisto RNA seq
qauntification tool "  
RUN apt-get update && apt-get install -y build-essential cmake zlib1g-dev
libhdf5-dev wget curl apt-utils unzip libncurses5-dev libncursesw5-dev
zlib1g-dev liblzma-dev libbz2-dev  
  
#install git  
RUN apt-get install --yes git  
  
# install Kallisto from github repo  
RUN git clone https://github.com/pachterlab/kallisto.git \  
&& cd kallisto \  
&& git checkout 5c5ee8a45d6afce65adf4ab18048b40d527fcf5c \  
&& mkdir build \  
&& cd build \  
&& cmake .. \  
&& make \  
&& make install \  
&& cd ../../ \  
&& rm -rf /var/lib/apt/lists/*  
  
# install samtools from binary repo  
#RUN wget
"https://github.com/samtools/samtools/releases/download/1.7/samtools-1.7.tar.bz2"
. \  
#&& tar xfj samtools-1.7.tar.bz2 \  
#&& cd samtools-1.7 \  
#&& make \  
#&& cp samtools /usr/bin  
# Setup ENV variables  
ENV SAMTOOLS_BIN="samtools-1.7.tar.bz2" \  
SAMTOOLS_VERSION="1.7"  
# Install SAMTools  
RUN curl -fsSL
https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VERSION/$SAMTOOLS_BIN
-o /opt/$SAMTOOLS_BIN \  
&& tar xvjf /opt/$SAMTOOLS_BIN -C /opt/ \  
&& cd /opt/samtools-$SAMTOOLS_VERSION \  
&& make \  
&& make install \  
&& rm /opt/$SAMTOOLS_BIN  
  
ADD Kallisto_align.pl /usr/bin/  
RUN [ "chmod", "+x", "/usr/bin/Kallisto_align.pl" ]  
ENTRYPOINT ["Kallisto_align.pl"]  

