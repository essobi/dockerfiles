FROM ubuntu:14.04  
MAINTAINER Dennis Hazelett "dennis.hazelett@csmc.edu"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN apt-get install -y zip unzip aria2 git  
  
RUN useradd -m user1  
RUN chown -R user1:staff /home/user1  
  
## SPP is not curated by either bioconductor or CRAN  
## it must be directly installed from a sourceforge repo  
## depends: libboost  
RUN apt-get install -y r-base-core libboost-dev  
RUN R -e "install.packages(pkgs=c('bitops', 'caTools'),
repos='http://cran.us.r-project.org', quiet=TRUE)"  
  
## download and install SPP  
RUN echo 'http://compbio.med.harvard.edu/Supplements/ChIP-seq/spp_1.11.tar.gz'
> sppfile \  
&& aria2c -x 10 -j 10 -s 10 -i sppfile \  
&& rm sppfile  
RUN R CMD INSTALL spp_1.11.tar.gz  
  
## install dependencies for MUSIC  
RUN apt-get install -y wget python-pip bedtools samtools python-dev libpython-
dev libevent-dev  
RUN pip install numpy  
RUN pip install macs2  
  
## download and install MUSIC software  
RUN su user1  
RUN cd /home/user1 \  
&& git clone https://github.com/gersteinlab/MUSIC \  
&& cd /home/user1/MUSIC \  
&& make clean \  
&& make \  
&& cd /home/user1 \  
&& git clone https://bitbucket.org/dennishazelett/peak  
  
## download and install HOMER software  
##  
RUN mkdir /home/user1/homer \  
&& cd /home/user1/homer \  
&& wget http://homer.salk.edu/homer/configureHomer.pl \  
&& perl configureHomer.pl -install homer \  
&& echo "PATH=$PATH:/home/user1/homer/.//bin/" >> /home/user1/.bashrc  
  

