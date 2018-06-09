FROM alpine  
MAINTAINER Subak Systems <info@subak.jp>  
  
ARG OCAML_VERSION=4.02.3  
ARG UNISON_VERSION=2.48.3  
RUN apk add --update build-base curl  
  
# ocaml  
RUN curl http://caml.inria.fr/pub/distrib/ocaml-$(echo ${OCAML_VERSION} | sed
's/\\.[0-9]*$//')/ocaml-${OCAML_VERSION}.tar.gz \  
| tar zxv -C /tmp \  
&& cd /tmp/ocaml-${OCAML_VERSION} \  
&& ./configure -with-debug-runtime -no-graph \  
&& make world.opt \  
&& make install  
  
# unison  
RUN curl
https://www.seas.upenn.edu/~bcpierce/unison//download/releases/stable/unison-${UNISON_VERSION}.tar.gz
\  
| tar zxv -C /tmp \  
&& cd /tmp/unison-${UNISON_VERSION} \  
&& sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/'
fsmonitor/linux/inotify_stubs.c \  
&& make UISTYLE=text \  
&& cp unison unison-fsmonitor /usr/local/bin  
  
RUN apk del build-base curl \  
&& rm -rfv /tmp/ocaml-${OCAML_VERSION} /tmp/unison-${UNISON_VERSION}  
  
ENV TZ Asia/Tokyo  
ENV LANG C.UTF-8  
EXPOSE 5000  
ENTRYPOINT ["unison","-socket"]  
CMD ["5000"]  

