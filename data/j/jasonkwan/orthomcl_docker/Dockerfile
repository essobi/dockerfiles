FROM appcontainers/mysql:debian  
MAINTAINER Jason C. Kwan "jason.kwan@wisc.edu"  
RUN apt-get update  
RUN apt-get install -y wget cpanminus build-essential libmysqlclient-dev
python  
RUN wget http://www.micans.org/mcl/src/mcl-latest.tar.gz  
RUN tar xvf mcl-latest.tar.gz  
RUN cd mcl-* && ./configure && make && make install  
RUN wget
http://orthomcl.org/common/downloads/software/v2.0/orthomclSoftware-v2.0.9.tar.gz  
RUN tar xvf orthomclSoftware-v2.0.9.tar.gz  
RUN cpanm DBI DBD::mysql  
RUN mkdir diamond && cd diamond && wget
http://github.com/bbuchfink/diamond/releases/download/v0.9.14/diamond-
linux64.tar.gz && tar xvf diamond-linux64.tar.gz  
RUN rm *.tar.gz  
  
COPY my.cnf /etc/mysql/  
COPY run_orthomcl.py /bin/  
ENV PATH="/diamond:/orthomclSoftware-v2.0.9/bin:${PATH}"  

