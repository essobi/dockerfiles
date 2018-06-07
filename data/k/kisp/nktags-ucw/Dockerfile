FROM dparnell/minimal-sbcl:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y emacs-nox git  
  
# RUN sbcl --eval '(sb-ext:disable-debugger)' --eval '(ql:update-client
:prompt nil)' --eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:update-all-dists
:prompt nil)' \--eval '(quit)'  
  
RUN ln -s /opt/quicklisp /root/quicklisp  
  
# pauldist  
ADD docker/quicklisp-setup-pauldist.lisp /tmp/quicklisp-setup-pauldist.lisp  
RUN sbcl --script /tmp/quicklisp-setup-pauldist.lisp  
RUN rm /tmp/quicklisp-setup-pauldist.lisp  
  
# quickload  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload
"bknr.datastore")' \--eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload "sqlite")'
\--eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload "ucw-
github-auth")' \--eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload "arnesi")'
\--eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload "s-xml-
rpc")' \--eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload "fiveam")'
\--eval '(quit)'  
RUN sbcl --eval '(sb-ext:disable-debugger)' \--eval '(ql:quickload "quicklisp-
slime-helper")' \--eval '(quit)'  
  
RUN mkdir /src  
ADD . /src  
WORKDIR /src  
  
RUN make test  
  
RUN sbcl --no-sysinit --no-userinit --eval "(require 'asdf)" \--eval '(sb-
ext:disable-debugger)' \--load snippets/setup-asdf.lisp --eval "(asdf:oos
'asdf:load-op :nktags-ucw)" \--eval "(ucw:create-server)" \--eval '(quit)'  
  
CMD make  

