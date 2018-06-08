FROM debian:sid  
  
RUN apt-get update  
RUN apt-get -y install perl wget git bzip2 make gcc tar  
  
RUN git clone git://github.com/geocol/perl-mediawiki-parser  
RUN cd perl-mediawiki-parser && PMBP_DUMP_BEFORE_DIE=1 make deps
PMBP_OPTIONS=--execute-system-package-installer  
ADD server.sh server  
RUN chmod u+x /server  
  
RUN echo '{"ja": {"cache_dir_name": "/perl-mediawiki-
parser/local/wpserver/cache/ja", "dump_file_name": "/perl-mediawiki-
parser/local/wpserver/xml/ja.xml"}}' > /keys.json  
  
RUN cd perl-mediawiki-parser && make -f Makefile.data data-ja  

