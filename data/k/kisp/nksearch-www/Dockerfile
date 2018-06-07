FROM dparnell/minimal-sbcl:latest  
  
# RUN sbcl --eval '(sb-ext:disable-debugger)' --eval '(ql:update-client
:prompt nil)' --eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:update-all-dists
:prompt nil)' \--eval '(quit)'  
  
RUN ln -s /opt/quicklisp /root/quicklisp  
  
RUN sbcl --eval '(ql:quickload "hunchentoot")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "cl-who")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "bknr.datastore")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "cl-ppcre")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "puri")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "html-template")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "babel")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "drakma")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "yason")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "do-urlencode")' \--eval '(quit)'  
  
RUN mkdir /src  
  
ADD . /src  
  
WORKDIR /src  
  
COPY docker/config.lisp config.lisp  
  
RUN mkdir /log  
RUN mkdir /store  
  
CMD sbcl --load load.lisp --load config.lisp --eval '(in-package :src)'
\--eval '(start)'  

