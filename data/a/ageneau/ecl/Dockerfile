FROM ageneau/devel-base:latest  
  
MAINTAINER Sylvain Ageneau <ageneau@gmail.com>  
  
RUN apt-get install -y --no-install-recommends git \  
wget \  
curl \  
locales \  
less  
  
RUN apt-get install -y --no-install-recommends libatomic-ops-dev \  
libffi-dev \  
libgc-dev \  
libgmp-dev \  
libncurses5-dev \  
texinfo  
  
RUN apt-get install -y --no-install-recommends ca-certificates  
RUN apt-get clean && apt-get autoclean  
  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
WORKDIR /project  
RUN git clone -b ECL-16.1.2 --recursive --depth=1
https://gitlab.com/embeddable-common-lisp/ecl.git  
WORKDIR /project/ecl  
RUN ./configure  
RUN make all install  
WORKDIR /project  
RUN rm -rf /project/ecl  
  
ENV LC_ALL C.UTF-8  
CMD ["ecl"]  

