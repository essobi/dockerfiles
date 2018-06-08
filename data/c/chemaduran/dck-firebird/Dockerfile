FROM phusion/baseimage  
  
MAINTAINER Chema Durán <jgduran@gmail.com>  
  
RUN apt-get update && apt-get install -y wget libncurses5-dev gcc g++ make;  
  
WORKDIR /home  
  
# Download firebird sources  
RUN wget --header='Host: softlayer-ams.dl.sourceforge.net' \--header='User-
Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101
Firefox/32.0' \--header='Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
\--header='Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
\--header='Referer:
http://sourceforge.net/projects/firebird/files/firebird/2.5.3-Release/Firebird-2.5.3.26778-0.tar.bz2/download'
\--header='Cookie:
__utma=191645736.632935831.1410779128.1410779128.1410779128.1;
__utmb=191645736.3.9.1410779131615; __utmc=191645736;
__utmz=191645736.1410779128.1.1.utmcsr=firebirdsql.org|utmccn=(referral)|utmcmd=referral|utmcct=/en/firebird-2-5-3/'
\--header='Connection: keep-alive' 'http://softlayer-
ams.dl.sourceforge.net/project/firebird/firebird/2.5.3-Release/Firebird-2.5.3.26778-0.tar.bz2'
-O 'firebird.tar.bz2' -c  
  
RUN tar xvjf firebird.tar.bz2; rm firebird.tar.bz2;  
  
WORKDIR /home/Firebird-2.5.3.26778-0  
  
RUN ./configure; make;  
  
WORKDIR /home/Firebird-2.5.3.26778-0/gen/firebird  
  
RUN cp ../install/misc/firebird.conf .; cp ../install/misc/fbintl.conf intl;
cp intl/libfbintl.so lib/fbintl.so  
  
ENV FIREBIRD /home/Firebird-2.5.3.26778-0/gen/firebird  
ENV PATH $FIREBIRD/bin:$PATH  
ENV LD_LIBRARY_PATH $FIREBIRD/lib  
  
VOLUME ["/databases"]  
  
ENTRYPOINT ["fbguard"]  
  
EXPOSE 3050  

