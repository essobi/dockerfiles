FROM paulhilbert/wp4_wp5_stripped_base:latest  
MAINTAINER Richard Vock <vock@cs.uni-bonn.de>  
ADD docker_build.sh /tmp/build.sh  
RUN /bin/sh /tmp/build.sh e57_metadata  
ENTRYPOINT ["e57_metadata_extractor"]  

