FROM frasertweedale/proofgeneral-coq  
MAINTAINER Fraser Tweedale <frase@frase.id.au>  
  
RUN yum install -y make && yum clean all  
RUN curl http://www.cis.upenn.edu/~bcpierce/sf/current/sf.tar.gz | tar xz  
ENTRYPOINT proofgeneral sf/Basics.v  

