FROM swflint/sbcl-centos  
MAINTAINER Sam Flint <swflint@flintfam.org>  
RUN echo "(require 'asdf)(require 'asdf-install)(asdf-install:install
\"http://common-
lisp.net/~loliveira/tarballs/inofficial/slime-2008-08-18.tar.gz\")" > sbcl  
RUN echo "(require 'asdf)" >> ~/.sbclrc  
RUN echo "(asdf:oos 'asdf:load-op 'swank)" >> ~/.sbclrc  
RUN echo "(setf swank:*use-dedicated-output-stream* nil)" >> ~/.sbclrc  
RUN echo "(setf swank:*communication-style* :fd-handler)" >> ~/.sbclrc  
RUN echo "(swank:create-server :dont-close t)" >> ~/.sbclrc  
ENTRYPOINT ["sbcl"]  
EXPOSE 22 80 4005

