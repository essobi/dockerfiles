FROM lambdasakura/ubuntu-cim  
MAINTAINER lambda_sakura  
RUN apt-get update  
RUN apt-get install -y build-essential time rlwrap  
RUN /bin/bash -c "source /cim/init.sh && cim install sbcl"  
CMD /bin/bash -c "source /cim/init.sh && cim use sbcl && rlwrap sbcl --load
/cim/quicklisp/setup.lisp"  
  

