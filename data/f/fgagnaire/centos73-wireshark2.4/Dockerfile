FROM fgagnaire/centos73-wireshark-build:latest  
  
  
MAINTAINER francis gagnaire  
USER root  
  
  
  
  
RUN git clone https://github.com/FAIG2014/wireshark.git wireshark-2.4 \  
&& cd wireshark-2.4 \  
&& git checkout master-2.4 \  
&& ./autogen.sh \  
&& /wireshark-2.4/configure \  
&& make -j 4 \  
&& make install \  
&& ldconfig  
  
ENTRYPOINT ["wireshark"]  
  

