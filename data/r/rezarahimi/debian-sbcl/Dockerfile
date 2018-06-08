## -*- docker-image-name: "rezarahimi/debian-sbcl" -*-  
  
FROM rezarahimi/debian  
MAINTAINER Reza Rahimi <rezarahimi@gmail.com>  
  
# SBCL Version  
ENV SBCL_VERSION_MAJOR 1  
ENV SBCL_VERSION_MINOR 2  
ENV SBCL_VERSION_BUILD 16  
ENV GIT_TAG
sbcl-${SBCL_VERSION_MAJOR}.${SBCL_VERSION_MINOR}.${SBCL_VERSION_BUILD}  
  
# Download and make SBCL  
RUN apt-get update && apt-get install -y curl git coreutils make gcc build-
essential sbcl time zlib1g-dev texlive texinfo rlwrap &&\  
echo "alias sbcl='rlwrap sbcl'" >> ~/.bashrc && \  
echo "alias ll='ls -alF'" >> ~/.bashrc && \  
git clone git://git.code.sf.net/p/sbcl/sbcl && \  
cd /sbcl && \  
git checkout -b ${GIT_TAG} tags/${GIT_TAG} && \  
sh make.sh \--fancy && \  
cd /sbcl/doc/manual && \  
make && \  
cd /sbcl && \  
sh install.sh && \  
rm -rf /sbcl && \  
wget -O /tmp/quicklisp.lisp "https://beta.quicklisp.org/quicklisp.lisp" && \  
wget -O /tmp/quicklisp.lisp.asc
"https://beta.quicklisp.org/quicklisp.lisp.asc" && \  
#gpg --verify /tmp/quicklisp.lisp.asc /tmp/quicklisp.lisp && \  
sbcl --load /tmp/quicklisp.lisp \  
\--eval '(quicklisp-quickstart:install)' \  
\--eval '(ql:add-to-init-file)' \  
\--eval '(quit)'  
  
CMD [ "/bin/bash" ]  

