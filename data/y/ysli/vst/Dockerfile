FROM ysli/coq  
ENV VST_VERSION master  
RUN . ~/.profile \  
&& git clone -b $VST_VERSION https://github.com/PrincetonUniversity/VST.git \  
&& make -C VST -j8  

