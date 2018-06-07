FROM quay.io/actcat/buildpack_android:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# install Opam for Infer  
# @see https://github.com/facebook/infer/blob/master/INSTALL.md  
RUN apt-get install -y git m4 zlib1g-dev python-software-properties build-
essential libgmp-dev libmpfr-dev libmpc-dev unzip  
RUN wget
https://github.com/ocaml/opam/releases/download/1.2.2/opam-1.2.2-x86_64-Linux
-O opam  
RUN chmod +x opam  
RUN ./opam init -y --comp=4.01.0  
ENV CAML_LD_LIBRARY_PATH "/root/.opam/4.01.0/lib/stublibs"  
ENV MANPATH "/root/.opam/4.01.0/man:"  
ENV PERL5LIB "/root/.opam/4.01.0/lib/perl5"  
ENV OCAML_TOPLEVEL_PATH "/root/.opam/4.01.0/lib/toplevel"  
ENV PATH "/root/.opam/4.01.0/bin:/usr/local/android-sdk-
linux/tools:/usr/local/android-sdk-linux/platform-
tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
RUN ./opam install -y extlib.1.5.4 atdgen.1.6.0 javalib.2.3.1 sawja.1.5.1  
  
# Install Infer  
RUN wget https://github.com/facebook/infer/releases/download/v0.3.0/infer-
linux64-v0.3.0.tar.xz  
RUN tar xf infer-*-v0.3.0.tar.xz  
RUN mv infer-linux64-v0.3.0 infer  
WORKDIR /root/work/infer  
RUN apt-get install -y rsync  
RUN make -C infer  
ENV PATH /root/work/infer/infer/bin:$PATH  
  

