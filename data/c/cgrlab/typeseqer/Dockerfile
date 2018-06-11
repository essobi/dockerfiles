FROM cgrlab/tidyverse:v1.0.0-beta.1706260830  
RUN apt-get update && apt-get install -y \  
git \  
pandoc \  
texlive-latex-recommended \  
texlive-latex-extra \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
autoconf \  
automake \  
make \  
g++ \  
gcc \  
build-essential \  
zlib1g-dev \  
libgsl0-dev \  
perl \  
curl \  
wget \  
unzip \  
tabix \  
libncurses5-dev \  
samtools  
  
# download and unarchive rabix  
RUN wget
https://github.com/rabix/bunny/releases/download/v1.0.4-3/rabix-1.0.4.tar.gz
&& \  
tar -xvzf rabix-1.0.4.tar.gz && \  
ln -s /rabix-cli-1.0.4/rabix /usr/local/bin/rabix  
  
# pandoc  
RUN wget
https://github.com/jgm/pandoc/releases/download/2.0.1.1/pandoc-2.0.1.1-1-amd64.deb
\  
&& dpkg -i pandoc-2.0.1.1-1-amd64.deb  
  
# bwa  
RUN git clone https://github.com/lh3/bwa && \  
cd bwa && \  
git checkout 0.7.10 && \  
make && cp bwa /usr/local/bin/bwa  
  
# sambamba  
RUN wget
https://github.com/biod/sambamba/releases/download/v0.6.6/sambamba_v0.6.6_linux.tar.bz2
&& \  
tar xvjf sambamba_v0.6.6_linux.tar.bz2  
  
# several R packages  
RUN echo 'source("https://bioconductor.org/biocLite.R");
biocLite("GenomicAlignments")' | r \  
&& echo 'require(devtools); devtools::install_github("tidyverse/tidyverse")' |
r \  
&& echo 'install.packages("knitr")' | r \  
&& echo 'require(devtools); devtools::install_github("rstudio/rmarkdown")' | r
\  
&& echo 'install.packages("pandoc")' | r \  
&& echo 'install.packages("pander")' | r \  
&& echo 'install.packages("koRpus")' | r \  
&& echo 'install.packages("fuzzyjoin")' | r \  
&& echo 'install.packages("ggsci")' | r \  
&& echo 'require(tidyverse); sessionInfo()' | r  
  
### Installing Java 8.... dockerfile snippet from
https://github.com/dockerfile/java/blob/master/oracle-java8/Dockerfile  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JAVA_LIBRARY_PATH /usr/lib/jni  
  
RUN mkdir TypeSeqer && cd TypeSeqer && git init && git pull
https://86e728b5c68508d0de00422e81126de37c118fbd@github.com/davidroberson/TypeSeqer-
private.git  
  
RUN cp /TypeSeqer/apps/* /TypeSeqer/docs/* /TypeSeqer/scripts/* /opt  
#RUN rm -R /TypeSeqer  
RUN mkdir /typeSeqerFiles  

