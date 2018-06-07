FROM kino/conts:deb  
ENV VVV=/usr/local/docker  
ENV VER=20.0  
ADD kerl /usr/bin/kerl  
RUN (mkdir -p $VVV; \  
kerl list releases; \  
env KERL_CONFIGURE_OPTIONS=--enable-halfword-emulator kerl build $VER
${VER}_halfword)  
RUN kerl install ${VER}_halfword $VVV/erl.${VER}  
  
EXPOSE 22  
CMD ["/usr/local/startservice.sh"]  
  

