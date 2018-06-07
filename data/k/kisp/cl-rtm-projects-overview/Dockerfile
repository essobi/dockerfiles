FROM dparnell/minimal-sbcl:latest  
  
RUN rm /etc/localtime ; ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
  
RUN sbcl --eval '(ql:quickload "drakma")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "yason")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "optima")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "alexandria")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "hunchentoot")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "cl-who")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "cl-ppcre")' \--eval '(quit)'  
RUN sbcl --eval '(ql:quickload "local-time")' \--eval '(quit)'  
  
RUN mkdir /src  
  
ADD . /src  
  
WORKDIR /src  
  
RUN sbcl --load load.lisp --eval '(quit)'  
  
RUN sbcl --load build.lisp  
  
CMD /src/app  

