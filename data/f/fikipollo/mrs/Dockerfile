############################################################  
# Dockerfile to build MRS container image for the eBioKit  
# Based on ubuntu:14.04  
# Version 0.1 August 2017  
# TODO LIST:  
# - Clean data to reduce image size  
############################################################  
  
# Set the base image to ubuntu:14.04  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Rafael Hernandez <https://github.com/fikipollo>  
  
################## BEGIN INSTALLATION ######################  
  
RUN apt-get update \  
&& apt-get install -y make g++ libboost-all-dev libzeep-dev libbz2-dev
libsqlite3-dev libperl-dev clustalo liblog4cpp5-dev wget rsync \  
&& apt-get clean  
  
RUN wget -O /tmp/mrs.tgz ftp://ftp.cmbi.ru.nl/pub/software/mrs/mrs-6.0.5.tgz \  
&& tar xzvf /tmp/mrs.tgz -C /tmp \  
&& cd /tmp/mrs-release-6.0.5/ \  
&& ./configure --data-dir=/data/mrs-data --log-dir=/log/mrs-log --base-url="/"
\  
&& make; exit 0  
  
RUN cd /tmp/mrs-release-6.0.5/ \  
&& /usr/bin/g++ -o mrs -I. obj/M6BitStream.o obj/M6Blast.o obj/M6BlastCache.o
obj/M6Builder.o obj/M6CmdLineDriver.o obj/M6Config.o obj/M6Log.o
obj/M6Databank.o obj/M6DataSource.o obj/M6Dictionary.o obj/M6DocStore.o
obj/M6Document.o obj/M6Error.o obj/M6Exec.o obj/M6Fetch.o obj/M6File.o
obj/M6Index.o obj/M6Iterator.o obj/M6Lexicon.o obj/M6Matrix.o obj/M6MD5.o
obj/M6Parser.o obj/M6Progress.o obj/M6Query.o obj/M6Server.o obj/M6Tokenizer.o
obj/M6Utilities.o obj/M6WSBlast.o obj/M6WSSearch.o -L /usr/lib -lzeep
-lboost_system -lboost_thread -lboost_filesystem -lboost_regex
-lboost_math_c99 -lboost_math_c99f -lboost_program_options -lboost_date_time
-lboost_iostreams -lboost_timer -lboost_random -lboost_chrono -lm -lpthread
-lrt -lz -lbz2 -llog4cpp -g -Wl,-E -fstack-protector -L/usr/local/lib
-L/usr/lib/perl/5.18/CORE -lperl -ldl -lm -lpthread -lc -lcrypt \  
&& make install \  
&& rm -r /tmp/*  
  
COPY configs/entrypoint.sh /usr/bin/entrypoint.sh  
  
RUN echo "root\n123\n123" | /usr/local/bin/mrs password \  
&& cd /data \  
&& tar -cvzf mrs-data.tgz mrs-data/ \  
&& mv mrs-data.tgz /usr/local/etc/mrs/ \  
&& chmod +x /usr/bin/entrypoint.sh  
  
##################### INSTALLATION END #####################  
  
EXPOSE 18090  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

