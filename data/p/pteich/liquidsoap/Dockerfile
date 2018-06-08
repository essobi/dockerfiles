FROM debian:jessie  
MAINTAINER Peter Teich <peter.teich@gmail.com>  
  
ENV OCAML_VERSION 4.02.3  
RUN \  
apt-get update && \  
apt-get install -q -y curl wget git make autoconf automake && \  
apt-get install -q -y libpcre3-dev libao-dev libmad0-dev libshout3-dev
libvorbis-dev libid3tag0-dev libasound2-dev liblo-dev libfaad-dev \  
libflac-dev ladspa-sdk libsoundtouch-dev libjack-dev libsamplerate0-dev
libtag1-dev \  
lame libmp3lame-dev libshine-dev libopus-dev libschroedinger-dev libvo-aacenc-
dev libportaudio-ocaml-dev libpulse-ocaml-dev \  
libgstreamer-ocaml-dev libgavl-ocaml-dev libavutil-dev libswscale-dev
libfrei0r-ocaml-dev dssi-dev libfaad-dev \  
opam ocaml-findlib libpcre-ocaml-dev libtool && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" && \  
chmod +x /usr/local/bin/gosu  
  
RUN adduser --disabled-password --gecos '' liquidsoap  
USER liquidsoap  
  
WORKDIR /home/liquidsoap  
  
RUN \  
git clone \--recursive https://github.com/savonet/liquidsoap-full.git && \  
opam init --comp $OCAML_VERSION  
  
ENV CAML_LD_LIBRARY_PATH "/home/liquidsoap/.opam/$OCAML_VERSION/lib/stublibs"  
ENV MANPATH "/home/liquidsoap/.opam/$OCAML_VERSION/man:$MANPATH"  
ENV MAKELEVEL ""  
ENV MAKEFLAGS ""  
ENV PERL5LIB "/home/liquidsoap/.opam/$OCAML_VERSION/lib/perl5"  
ENV OCAML_TOPLEVEL_PATH "/home/liquidsoap/.opam/$OCAML_VERSION/lib/toplevel"  
ENV PATH "/home/liquidsoap/.opam/$OCAML_VERSION/bin:$PATH"  
RUN opam install -y ocamlfind dtools duppy mm pcre xmlm camomile  
  
WORKDIR liquidsoap-full  
  
COPY ./PACKAGES ./  
  
RUN ./bootstrap && ./configure && make  
  
USER root  
  
RUN make install && rm -rf liquidsoap-full  
  
ENTRYPOINT ["/usr/local/bin/gosu","liquidsoap","/usr/local/bin/liquidsoap"]  
  
CMD ["--help"]  

