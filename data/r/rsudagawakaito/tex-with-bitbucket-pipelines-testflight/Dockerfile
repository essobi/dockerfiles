FROM frolvlad/alpine-glibc  
  
ENV
PATH=/usr/local/texlive/2016/bin/x86_64-linux:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN apk --no-cache add \  
perl \  
wget \  
xz  
RUN wget -qO- http://mirror.ctan.org/systems/texlive/tlnet/install-tl-
unx.tar.gz | tar -xz -C /tmp  
RUN printf 'selected_scheme scheme-basic\noption_doc 0\noption_src 0' >
/tmp/texlive.profile \  
&& /tmp/install-tl-*/install-tl -profile /tmp/texlive.profile  
RUN tlmgr option repository
http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet/ \  
&& tlmgr install collection-langjapanese \  
&& rm -fr /tmp/install-tl-* /tmp/texlive.profile \  
&& apk --no-cache del \  
perl \  
wget \  
xz \  
;  

