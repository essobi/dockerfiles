  
FROM ubuntu  
MAINTAINER Thai Pangsakulyanont <org.yi.dttvb@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
# useful for debugging...  
RUN apt-get install -y wget tmux  
  
# needed for crosstool-ng  
# arigatou: http://wwsean08.com/2012/05/15/how-to-build-a-custom-toolchain-
using-crosstool-ng/  
RUN apt-get install -y gperf bison flex texinfo gawk libtool automake
libncurses5-dev expat libexpat1-dev  
RUN apt-get install -y subversion  
  
# set up user for crosstool-ng  
RUN useradd crosstool -d /uchi  
RUN mkdir /uchi && chown crosstool /uchi  
USER crosstool  
ENV HOME /uchi  
  
# download crosstool  
RUN cd /uchi && wget http://crosstool-ng.org/download/crosstool-ng/crosstool-
ng-1.19.0.tar.bz2 && tar xvjf crosstool-ng-1.19.0.tar.bz2  
RUN mkdir /uchi/crosstool /uchi/kindle-toolchain /uchi/src  
RUN cd /uchi/crosstool-ng-1.19.0 && ./configure --prefix=/uchi/crosstool &&
make && make install  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/uchi/crosstool/bin  
  
# make kindle toolchain  
ADD ct-ng.my.config /ct-ng.config  
RUN cp /ct-ng.config /uchi/kindle-toolchain/.config  
RUN cd /uchi/kindle-toolchain && ct-ng build && cd /uchi && rm -rf
/uchi/kindle-toolchain  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/uchi/crosstool/bin:/uchi/x-tools/arm-
kindle_k5-linux-gnueabi/bin  
  

