FROM ubuntu:16.04  
# Install git, python and mysql server  
RUN apt-get update && apt-get install -y git python build-essential curl wget
mysql-client libmysqlclient-dev  
# Install orthoMcl with dependencies  
WORKDIR /root  
RUN wget -O - http://cpanmin.us | perl - --self-upgrade  
RUN cpanm Bio::Perl DBD::mysql DBI Parallel::ForkManager YAML::Tiny
Set::Scalar Text::Table Exception::Class Test::Most Test::Warn Test::Exception
Test::Deep Moose SVG Algorithm::Combinatorics  
RUN wget https://www.micans.org/mcl/src/mcl-14-137.tar.gz  
RUN tar xvfz mcl-14-137.tar.gz  
WORKDIR mcl-14-137  
RUN ./configure  
RUN make install  
WORKDIR /root  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz  
RUN tar xvfz ncbi-blast-2.6.0+-x64-linux.tar.gz  
RUN mv ncbi-blast-2.6.0+/bin/* /usr/local/bin  
RUN wget
http://orthomcl.org/common/downloads/software/v2.0/orthomclSoftware-v2.0.9.tar.gz  
RUN tar xvfz orthomclSoftware-v2.0.9.tar.gz  
RUN mv orthomclSoftware-v2.0.9/bin/* /usr/local/bin  
RUN mkdir /usr/local/lib/site_perl  
RUN mv orthomclSoftware-v2.0.9/lib/perl/* /usr/local/lib/site_perl  
RUN rm -rf orthomclSoftware-*/ ncbi-blast-*/ mcl-*/  
RUN apt-get remove -y build-essential curl wget  
RUN apt-get autoremove -y  
# Finally install orthoMcl wrapper and the startup script  
WORKDIR /root  
RUN git clone \--recursive git://github.com/vetscience/Tools  
WORKDIR Tools  
COPY orthoMcl .  
RUN chmod uog+x /root && chmod uog+rwx /root/Tools && chmod uog+x orthoMcl  
ENTRYPOINT ["/root/Tools/orthoMcl"]  

