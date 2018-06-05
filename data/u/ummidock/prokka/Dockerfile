FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
  
WORKDIR /NGStools/  
  
# Dependencies  
RUN apt-get update && apt-get upgrade -y perl && apt-get install -y parallel
make wget git python-pip locales && pip install -U setuptools && locale-gen
--purge en_US.UTF-8 && DEBIAN_FRONTEND="noninteractive" dpkg-reconfigure
locales && update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8
LC_ALL=en_US.UTF-8  
  
# Barrnap  
RUN wget https://github.com/tseemann/barrnap/archive/0.8.tar.gz && tar xf
0.8.tar.gz && rm 0.8.tar.gz  
  
# Infernal  
RUN wget http://eddylab.org/infernal/infernal-1.1.2-linux-intel-gcc.tar.gz &&
tar xf infernal-1.1.2-linux-intel-gcc.tar.gz && rm infernal-1.1.2-linux-intel-
gcc.tar.gz && cd infernal-1.1.2-linux-intel-gcc && ./configure && make && make
install && cd easel && make install && cd /NGStools && rm -rf
infernal-1.1.2-linux-intel-gcc/  
  
# GenomeTools  
RUN apt-get install -y libpango1.0-dev && wget
http://genometools.org/pub/genometools-1.5.9.tar.gz && tar xf
genometools-1.5.9.tar.gz && rm genometools-1.5.9.tar.gz && cd
genometools-1.5.9 && make && make install && cd gtpython && python setup.py
install && cd /NGStools && rm -rf genometools-1.5.9/  
  
# gff3toembl  
RUN mkdir gff3toembl && cd gff3toembl && git clone https://github.com/sanger-
pathogens/gff3toembl.git && python gff3toembl/setup.py install && cd /NGStools  
  
# Blast+  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz && tar xf ncbi-blast-2.6.0+-x64-linux.tar.gz &&
rm ncbi-blast-2.6.0+-x64-linux.tar.gz  
  
# CD-HIT  
RUN wget https://github.com/weizhongli/cdhit/releases/download/V4.6.8/cd-
hit-v4.6.8-2017-0621-source.tar.gz && tar xf cd-
hit-v4.6.8-2017-0621-source.tar.gz && rm cd-hit-v4.6.8-2017-0621-source.tar.gz
&& cd cd-hit-v4.6.8-2017-0621 && make && cd cd-hit-auxtools && make && cd
/NGStools  
  
# Exonerate  
RUN wget
http://ftp.ebi.ac.uk/pub/software/vertebrategenomics/exonerate/exonerate-2.2.0-x86_64.tar.gz
&& tar xf exonerate-2.2.0-x86_64.tar.gz --no-same-owner && chmod 755
exonerate-2.2.0-x86_64/ && rm exonerate-2.2.0-x86_64.tar.gz  
  
# Prokka  
RUN apt-get install -y libdatetime-perl libxml-simple-perl libdigest-md5-perl
default-jre bioperl && git clone https://github.com/tseemann/prokka.git &&
prokka/bin/prokka --setupdb  
  
# tbl2asn  
RUN wget
ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux.tbl2asn.gz
&& \  
gunzip linux.tbl2asn.gz && \  
mv linux.tbl2asn tbl2asn && \  
chmod +x tbl2asn && \  
mv tbl2asn /NGStools/prokka/binaries/linux/  
  
# Sequin not install because it requires X Windows  
# Be aware that EMBL validator changed. Please see
http://www.ebi.ac.uk/ena/software/flat-file-validator for further information  
ENV PATH="/NGStools/gff3toembl/gff3toembl/scripts:/NGStools/ncbi-
blast-2.6.0+/bin:/NGStools/cd-hit-v4.6.8-2017-0621:/NGStools/cd-
hit-v4.6.8-2017-0621/cd-hit-
auxtools:/NGStools/exonerate-2.2.0-x86_64/bin:/NGStools/prokka/bin:${PATH}"
LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
PYTHONPATH="/NGStools/gff3toembl/gff3toembl:$PYTHONPATH"  
# Clean  
RUN pip uninstall -y setuptools && apt-get remove -y git python-pip locales &&
apt-get autoclean -y  
  
WORKDIR /data/  

