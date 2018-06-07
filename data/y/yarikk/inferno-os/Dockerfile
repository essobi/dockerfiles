FROM i386/gcc:6.1  
COPY . /usr/inferno/  
ENV PATH=$PATH:/usr/inferno/Linux/386/bin  
WORKDIR /usr/inferno  
RUN \  
MKFLAGS='SYSHOST=Linux OBJTYPE=386 ROOT='$PWD; \  
mk $MKFLAGS mkdirs && \  
mk $MKFLAGS emuinstall && \  
mk $MKFLAGS emunuke  
ENTRYPOINT ["emu"]  

