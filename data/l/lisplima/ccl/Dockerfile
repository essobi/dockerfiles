FROM debian:jessie  
  
ENV CCL_VERSION 1.10  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# XXX: /usr/local/src is the default "$CCL_DEFAULT_DIRECTORY"  
RUN mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& curl -SL
"ftp://ftp.clozure.com/pub/release/${CCL_VERSION}/ccl-${CCL_VERSION}-linuxx86.tar.gz"
| tar xzv --exclude='.svn' \--exclude='examples' \  
&& ln -s /usr/local/src/ccl/scripts/ccl64 /usr/local/bin/ccl  
  
RUN curl -SLO https://beta.quicklisp.org/release-key.txt \  
&& curl -SLO https://beta.quicklisp.org/quicklisp.lisp \  
&& curl -SLO https://beta.quicklisp.org/quicklisp.lisp.asc \  
&& gpg --import release-key.txt \  
&& gpg --verify quicklisp.lisp.asc quicklisp.lisp \  
&& echo "(quicklisp-quickstart:install)(let ((ql-util::*do-not-prompt*
t))(ql:add-to-init-file))(ccl:quit 0)" >> quicklisp.lisp \  
&& ccl --load quicklisp.lisp \  
&& rm release-key.txt quicklisp.lisp quicklisp.lisp.asc  
  
CMD [ "ccl" ]  

