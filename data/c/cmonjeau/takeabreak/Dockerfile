############################################################  
# Dockerfile to build Takeabreak tool container image  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc g++ zlib1g-dev  
  
ENV TAR
https://colibread.inria.fr/files/2014/01/TakeABreak-1.1.2-Source.tar_.gz  
ENV SOURCE TakeABreak-1.1.2-Source  
ENV DIR /opt  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## TAKEABREAK INSTALLATION ######################  
  
WORKDIR ${DIR}  
RUN wget ${TAR} -O - | tar xvzf -  
WORKDIR ${DIR}/${SOURCE}  
RUN /bin/bash INSTALL  
RUN cp build/TakeABreak /usr/local/bin  
  
ENTRYPOINT ["TakeABreak"]  
CMD ["--help"]  
  
##################### Maintainer #####################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  
  
#################### Example ########################  
# docker run -it --rm cmonjeau/takeabreak  
# docker run -it --rm -v /home/user/TakeABreak/files:/data cmonjeau/takeabreak
-in
'/data/toy_example.fasta,/data/toy_example_reads.fasta,/data/toy_example_with_inv.fasta,/data/toy_example_with_inv_reads.fasta'
-out /data/result  
  

