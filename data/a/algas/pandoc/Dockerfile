FROM fpco/stack-build:lts-9.9  
WORKDIR /usr/lib/gcc/x86_64-linux-gnu/5.4.0  
RUN cp crtbeginT.o crtbeginT.o.orig  
RUN cp crtbeginS.o crtbeginT.o  
ADD ./ /work  
WORKDIR /work  
RUN stack setup  
RUN stack --system-ghc --local-bin-path /sbin build --ghc-options '-optl-
static -fPIC -optc-Os'  
  
FROM alpine:latest  
RUN mkdir /work  
COPY \--from=0 /work/.stack-work /work/.stack-work  
COPY \--from=0 /work/.stack-work/install/x86_64-linux/lts-9.9/8.0.2/bin/pandoc
/sbin/  
CMD ["/sbin/pandoc"]  

