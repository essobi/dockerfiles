FROM paulhilbert/wp4_wp5_stripped_base:latest  
MAINTAINER Sebastian Ochmann <ochmann@cs.uni-bonn.de>  
ADD docker_build.sh /tmp/build.sh  
RUN /bin/sh /tmp/build.sh paulhilbert october  
RUN /usr/bin/ldconfig  
RUN /bin/sh /tmp/build.sh ochilan duraark_autoreg  
ENTRYPOINT ["autoreg"]  

