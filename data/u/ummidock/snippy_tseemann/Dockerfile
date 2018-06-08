FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
  
# Create a non root user  
RUN useradd --create-home --home-dir /NGStools/ ubuntu  
  
WORKDIR /NGStools/  
  
RUN apt-get update  
  
# Dependencies  
# For Bio Perl  
RUN apt-get install -y make cpanminus  
# Bio Perl  
RUN cpanm Bio::Perl  
# Java  
RUN apt-get install -y default-jre  
# For Linuxbrew  
RUN apt-get install -y build-essential curl file git python-setuptools ruby
locales && locale-gen en_US.UTF-8 && update-locale  
# Change to the non root user  
USER ubuntu  
# Linuxbrew  
RUN git clone https://github.com/Linuxbrew/brew.git /NGStools/linuxbrew  
ENV PATH="/NGStools/linuxbrew/bin:${PATH}"  
ENV MANPATH="/NGStools/linuxbrew/share/man:${MANPATH}"  
ENV INFOPATH="/NGStools/linuxbrew/share/info:${INFOPATH}"  
# Snippy  
RUN brew tap homebrew/science && brew tap tseemann/homebrew-bioinformatics-
linux && brew install snippy  
# Correct freebayes-parallel  
RUN sed -i "s#../vcflib/scripts/vcffirstheader#vcffirstheader#g"
/NGStools/linuxbrew/Cellar/freebayes/1.1.0/bin/freebayes-parallel && sed -i
"s#../vcflib/bin/vcfstreamsort#vcfstreamsort#g"
/NGStools/linuxbrew/Cellar/freebayes/1.1.0/bin/freebayes-parallel  
  
# Clean  
USER root  
RUN apt-get remove -y make cpanminus build-essential curl file git python-
setuptools ruby locales && apt-get autoclean -y  
  
WORKDIR /data/  
  
# CMD snippy --help  

