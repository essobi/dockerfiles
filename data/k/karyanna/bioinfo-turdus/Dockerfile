FROM debian:testing  
  
  
MAINTAINER Kary Ocana "karyanna@gmail.com"  
  
  
# =============  
# \--- Linux ---  
# =============  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y install wget --assume-yes apt-utils &&
apt-get -y install build-essential && apt-get install bash  
  
#RUN apt-get -y install build-essential  
#RUN apt-get -y install tar --assume-yes  
#RUN apt-get -y install zip --assume-yes  
#RUN apt-get -y install unzip --assume-yes  
#RUN apt-get -y install git --assume-yes  
#RUN apt-get -y install -f  
#RUN apt-get -y install gawk  
###RUN apt-get -y install devscripts build-essential  
#RUN apt-get -y install cpio  
  
# Libraries GenomeTools  
#RUN apt-get -y install libcairo2-dev && apt-get -y install libpango1.0-dev  
#RUN apt-get -y install zlib1g-dev --assume-yes  
#RUN apt-get -y install bzip2 --assume-yes  
##RUN apt-get -y install lib32z1 lib32ncurses5 libbz2-1.0:i386 lib32stdc++6
--assume-yes  
#RUN apt-get -y install liblua5.1-0 --assume-yes  
#RUN apt-get -y install lua-filesystem --assume-yes  
#RUN apt-get -y install lua-lpeg --assume-yes  
#RUN apt-get -y install lua-md5 --assume-yes  
#RUN apt-get -y install libexpat1 --assume-yes  
#RUN apt-get -y install libtre-dev --assume-yes  
#RUN apt-get -y install libsqlite3-dev --assume-yes  
#RUN apt-get -y install libbam-dev --assume-yes  
  
# Libraries Blast  
#RUN apt-get -y install gcc  
#RUN apt-get -y install libgtk-3-dev build-essential checkinstall  
#RUN apt-get -y install libncbi-vdb-dev  
#RUN apt-get -y install libunwind-setjmp0-dev  
#RUN apt-get -y install zsh  
#RUN apt-get -y install liblzo2-2 liblzo2-dev  
#RUN apt-get -y install libpcre3 libpcre3-dev  
#RUN apt-get -y install libmbedcrypto0 libmbedx509-0 libmbedtls-dev  
#RUN apt-get -y install libgmp3-dev  
#RUN apt-get -y install libgcrypt11-dev gcc #sudo apt-get install
libgcrypt11-dev #  
#RUN apt-get -y install nettle-dev  
#RUN apt-get -y install gnutls-bin  
#RUN apt-get -y install libssl-dev  
#RUN apt-get -y install libboost-all-dev libboost-dev  
#RUN apt-get -y install libffi-dev python-dev build-essential  
  
  
# ====================================  
# \--- MITE-Hunter AND Dependencies ---  
# ====================================  
  
###RUN apt-get -y install blast2  
###RUN apt-get -y install muscle  
###RUN wget
ftp://occams.dfci.harvard.edu/pub/bio/tgi/software/seqclean/mdust.tar.gz && \  
###tar -xvzf mdust.tar.gz && \  
###cd mdust && \  
###make  
  
# ====================================  
# \--- GenomeTools AND Dependencies ---  
# ====================================  
  
# GenomeTools  
###RUN apt-get -y install genometools  
###RUN apt-get -y install libgenometools0 libgenometools0-dev  
  
  
# ======================================  
# \--- RepeatMasker AND Dependencies ---  
# ======================================  
  
# RepeatMasker (http://www.repeatmasker.org/RMDownload.html)  
  
# HMMER (http://hmmer.org/)  
RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-
intel-x86_64.tar.gz && \  
tar xf hmmer-3.1b2-linux-intel-x86_64.tar.gz && \  
cd hmmer-3.1b2-linux-intel-x86_64 && \  
./configure && \  
make && \  
make check && \  
make install  
  
# For Cross_Match -> "databases/crossmatch"  
  
# RMBlast -> "databases/rmblast/bin"  
  
# WUBlast -> "databases/wublast_aurelie"  
  
# TRF "databases/trf"  
  
# Dfam (só precisa Updates)  
#RUN wget http://www.dfam.org/web_download/Release/Dfam_2.0/Dfam.hmm.gz && \  
# cp Dfam.hmm.gz /usr/local/RepeatMasker/Libraries && \  
# cd /usr/local/RepeatMasker/Libraries && \  
# gunzip Dfam.hmm.gz && \  
# rm Dfam.hmm.gz  
  
# RepeatMasker  
RUN wget http://www.repeatmasker.org/RepeatMasker-open-4-0-7.tar.gz && \  
cp RepeatMasker-open-4-0-7.tar.gz /usr/local && \  
cd /usr/local && \  
gunzip RepeatMasker-open-4-0-7.tar.gz && \  
tar xvf RepeatMasker-open-4-0-7.tar  
  
# Script for configuring volume and installing repeatmasker  
#CMD echo "Hello world"  
#ENTRYPOINT echo "Hello world"  
ENTRYPOINT ["/bin/echo", "Hello world kary"]  
  
#COPY scripts/install/install_repeatmasker.sh /  
#ENTRYPOINT ["/install_repeatmasker.sh"]  
  
#RUN cp /databases/RepBaseRepeatMaskerEdition-20170127.tar.gz
/usr/local/RepeatMasker/ && \  
# cd /usr/local/RepeatMasker && \  
# gunzip RepBaseRepeatMaskerEdition-20170127.tar.gz && \  
# tar xvf RepBaseRepeatMaskerEdition-20170127.tar && \  
# rm RepBaseRepeatMaskerEdition-20170127.tar  
  
# Run RepeatMasker Configure Script (depois que o "databases" estiver apontado
e todas as depências estiverem instaladas)  
###RUN cd /usr/local/RepeatMasker && \  
### perl ./configure  
#RUN scripts/install/install_repeatmasker.sh  
  
# enter to continue  
# Enter path [ /usr/bin/perl ]:  
# Enter path [ /usr/local/RepeatMasker ]: # Building Fasta database  
# Enter path [ /home/programs/trf ]:  
# Add a Search Engine:  
# 1\. CrossMatch: [ Un-configured ]  
# 2\. RMBlast - NCBI Blast with RepeatMasker extensions: [ Un-configured ]  
# 3\. WUBlast/ABBlast (required by DupMasker): [ Un-configured ]  
# 4\. HMMER3.1 & DFAM: [ Un-configured ]  
# 5\. Done  
# Enter Selection:  

