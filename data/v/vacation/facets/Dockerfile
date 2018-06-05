# Dockerfile for running MSK's facets  
#  
# v0.5.6 (latest 2017-08-28)  
#  
# Facets was distributed under GPL v2.0  
# cite:  
# Ronglai Shen and Venkatraman E. Seshan. FACETS: allele-specific  
# copy number and clonal heterogeneity analysis tool for  
# high-throughput DNA sequencing. Nucleic Acids Research,  
# Volume 44, Issue 16, 19 September 2016, Pages e131,  
# https://doi.org/10.1093/nar/gkw520  
# Start from locked in tidyverse since we need devtools  
FROM rocker/tidyverse:3.4.1  
# Now get their snp-pileup code working too and vignette building  
RUN apt-get update && apt-get -y install bzip2 build-essential zlib1g-dev
libbz2-dev liblzma-dev texinfo texlive  
  
#Get the actual program installed. Note that it will remote to get a
dependency  
RUN Rscript -e 'devtools::install_github("jason-weirather/facets",
build_vignettes = TRUE)'  
  
RUN mkdir /Source  
RUN cd /Source && git clone https://github.com/jason-weirather/facets.git  
COPY inst/extcode/htslib/htslib-1.5.tar.bz2 /Source/htslib-1.5.tar.bz2  
RUN cd /Source && tar -xjf htslib-1.5.tar.bz2  
RUN cd /Source/htslib-1.5 && ./configure && make && make install  
RUN cd /Source/facets/inst/extcode && g++ -std=c++11
-I/usr/local/include/htslib snp-pileup.cpp -L/usr/local/lib -lhts
-Wl,-rpath=/usr/local/lib -o snp-pileup  
ENV PATH="/Source/facets/inst/extcode:${PATH}"

