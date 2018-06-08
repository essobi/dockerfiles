FROM rocker/ropensci  
  
MAINTAINER Brian O'Meara <omeara.brian@gmail.com>  
  
ADD VERSION .  
  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
RUN echo 'options(repos = c(CRAN="https://cran.rstudio.com"))' > ~/.Rprofile  
  
RUN apt-get install -y software-properties-common  
  
RUN apt-get -y install python-dev  
  
RUN apt-get -y install libcgal-dev libglu1-mesa-dev libglu1-mesa-dev
libx11-dev  
  
RUN apt-get update  
RUN apt-get -y install x11-common  
  
RUN apt-get install -y libmpfr-dev libmpfr-doc  
  
RUN apt-get install -y curl  
  
RUN apt-get install libgl1-mesa-dev  
  
RUN apt-get install ed  
RUN apt-get install -y mafft  
  
RUN apt-get install -y muscle  
  
RUN apt-get install -y python-numpy  
  
RUN apt-get install -y python-scipy  
  
RUN apt-get install -y python-biopython  
  
RUN apt-get install dnsutils -y  
RUN pip install -U dendropy  
  
RUN apt-get install -y puppet  
  
RUN Rscript -e "install.packages('ctv')"  
RUN Rscript -e "ctv::install.views('Phylogenetics')"  
RUN Rscript -e "install.packages('diagram')"  
RUN Rscript -e "devtools::install_github('bomeara/phrapl')"  
RUN Rscript -e "devtools::install_github( 'heibl/ips')"  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R")'  
  
RUN Rscript -e "install.packages('yearn')"  
RUN mkdir /usr/local/pathd8download && \  
wget http://www2.math.su.se/PATHd8/PATHd8.zip -O
/usr/local/pathd8download/PATHd8.zip && \  
cd /usr/local/pathd8download && \  
unzip /usr/local/pathd8download/PATHd8.zip && \  
cc PATHd8.c -O3 -lm -o PATHd8 && \  
cp PATHd8 /usr/local/bin/PATHd8  
  
RUN mkdir /usr/local/supersmart && \  
cd /usr/local/supersmart && \  
git clone https://github.com/naturalis/supersmart.git && \  
cd supersmart/conf && \  
puppet apply  
  
  
# From https://github.com/Linuxbrew/docker/blob/master/centos7/Dockerfile  
RUN apt-get install -y curl make ruby sudo \  
&& apt-get clean all  
  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& useradd -m -s /bin/bash linuxbrew \  
&& echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers  
  
USER linuxbrew  
WORKDIR /home/linuxbrew  
  
ENV PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH
\  
SHELL=/bin/bash \  
USER=linuxbrew  
  
RUN yes | ruby -e "$(curl -fsSL
https://raw.githubusercontent.com/Linuxbrew/install/master/install)" \  
&& brew config  
  
  
RUN brew tap jonchang/biology  
  
# RUN brew install revbayes  
  
RUN brew install bucky  
  
RUN brew tap bomeara/homebrew-science  
  
RUN brew install -v treepl  
  
RUN brew install raxml  
  
RUN brew install phylip  
  
RUN brew install phyutility  
  
# RUN brew install phlawd  
  
# RUN brew install phylocom  
  
RUN brew install beast  
  
RUN brew install beast2  
  
RUN brew install prank  
  
RUN brew install trimal  
  
RUN brew install clustal-omega  
  
RUN brew install fasttree  
  
  
RUN cp /home/linuxbrew/.linuxbrew/bin/raxmlHPC-PTHREADS
/home/linuxbrew/.linuxbrew/bin/raxml && \  
cp /home/linuxbrew/.linuxbrew/bin/raxmlHPC-PTHREADS
/home/linuxbrew/.linuxbrew/bin/raxmlHPC  
  
USER root  
  
ENV PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH  
RUN mkdir /usr/local/phylocom && \  
wget https://github.com/downloads/phylocom/phylocom/phylocom-4.2.zip -O
/usr/local/phylocom/phylocom.zip && \  
cd /usr/local/phylocom && \  
unzip /usr/local/phylocom/phylocom.zip && \  
cd /usr/local/phylocom/phylocom-4.2/src && \  
make && \  
cp phylocom /usr/local/bin && \  
cp phylomatic /usr/local/bin  
  
  
RUN mkdir /usr/local/paup  
RUN wget http://phylosolutions.com/paup-test/paup4a159_ubuntu64.gz -O
/usr/local/paup/paup.gz  
RUN cd /usr/local/paup  
RUN gunzip /usr/local/paup/paup.gz  
RUN chmod u+x /usr/local/paup/paup  
RUN cp /usr/local/paup/paup /usr/local/bin/paup  

