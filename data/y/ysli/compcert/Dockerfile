FROM ysli/coq  
ENV COMPCERT_VERSION master  
RUN . ~/.profile \  
&& opam install menhir \  
&& git clone -b $COMPCERT_VERSION https://github.com/AbsInt/CompCert.git \  
&& cd CompCert \  
&& ./configure -clightgen -ignore-coq-version x86_64-linux \  
&& make \  
&& sudo make install  

