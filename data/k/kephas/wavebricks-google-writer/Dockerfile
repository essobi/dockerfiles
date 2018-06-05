FROM debian:unstable  
MAINTAINER Pierre Thierry <pierre@nothos.net>  
  
RUN apt-get update && apt-get install -y build-essential  
RUN apt-get install -y wget \  
sbcl \  
git \  
nodejs \  
npm  
  
RUN npm install -g bower  
RUN wget http://beta.quicklisp.org/quicklisp.lisp  
RUN sbcl --load quicklisp.lisp --eval '(quicklisp-quickstart:install)' \--eval
'(let ((ql-util::*do-not-prompt* t))(ql:add-to-init-file))'  
RUN sbcl --eval '(ql-dist:install-dist
"http://beta.quicklisp.org/dist/quicklisp/2017-05-16/distinfo.txt" :prompt nil
:replace t)'  
  
# Ironclad takes time and MUST be cached  
RUN sbcl --eval '(ql:quickload "ironclad")'  
  
# Pre-load common dependencies/tools for caching purposes  
RUN git clone https://github.com/kephas/cl-scheme.git /root/quicklisp/local-
projects/cl-scheme  
RUN git clone https://github.com/kephas/cl-docker-tools.git
/root/quicklisp/local-projects/cl-docker-tools  
RUN git clone https://github.com/kephas/cl-web-object-capabilities.git
/root/quicklisp/local-projects/cl-web-object-capabilities  
RUN git clone -b parse-uri https://github.com/kephas/cl-mongo.git
/root/quicklisp/local-projects/cl-mongo  
RUN sbcl --eval '(ql:register-local-projects)' \  
\--eval '(ql:quickload (list "scheme" "cl-docker-tools" "web-object-
capabilities" \  
"alexandria" "split-sequence" "metabang-bind" "hu.dwim.stefil" \  
"caveman2" "ningle" "cl-who" "drakma" "clack-handler-hunchentoot"))'  
  
# Pre-load remaining dependencies before COPY  
RUN sbcl --eval '(ql:quickload (list "cl-match" "cl-json"))'  
  
COPY ./ /root/quicklisp/local-projects/wavebricks-cl-google-writer/  
  
RUN sbcl --eval '(ql:register-local-projects)' \--eval '(ql:quickload
"wavebricks-cl-google-writer")' # Pre-compile the project  
  
ENV PORT=80  
CMD sbcl --eval '(ql:quickload (list "cl-docker-tools" "wavebricks-cl-google-
writer"))' \  
\--eval '(docker-tools:swank 4005)' \--eval "(wavebricks-cl-google-
writer/web:start-server)"  
EXPOSE 4005  
EXPOSE 80  

