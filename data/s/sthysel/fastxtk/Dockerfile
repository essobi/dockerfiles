# fastx_toolkit container  
# https://github.com/agordon/fastx_toolkit/  
#  
FROM sthysel/bioshopcommon  
MAINTAINER sthysel <sthysel@gmail.com>  
ENV REFRESHED_AT 2015-08-28  
ENV BUILD_HOME /build/  
  
RUN apt-get install -y --no-install-recommends \  
perl \  
unzip \  
gnuplot \  
zlib1g-dev \  
libgd-dev \  
libgd-perl \  
automake \  
libtool \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN env --unset=DEBIAN_FRONTEND  
  
RUN mkdir ${BUILD_HOME}  
  
# build gordon text utils from source  
WORKDIR ${BUILD_HOME}  
RUN wget https://github.com/agordon/libgtextutils/archive/master.zip  
RUN unzip master.zip && rm master.zip  
WORKDIR ${BUILD_HOME}/libgtextutils-master/  
RUN autoreconf --install --force && \  
automake --force-missing --add-missing && \  
./configure && \  
make && \  
make install  
  
# build fastx_toolkit from source  
WORKDIR ${BUILD_HOME}  
RUN wget https://github.com/agordon/fastx_toolkit/archive/master.zip  
RUN unzip master.zip && rm master.zip  
WORKDIR ${BUILD_HOME}/fastx_toolkit-master/  
RUN autoreconf --install --force && \  
automake --force-missing --add-missing && \  
./configure && \  
make && \  
make install  
  
# mount volume here  
VOLUME /data  
WORKDIR /data  
  
CMD ["/bin/bash"]  

