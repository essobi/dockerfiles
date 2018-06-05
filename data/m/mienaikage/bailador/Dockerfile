FROM alpine:3.6  
RUN apk update && apk add perl git gcc musl-dev make linux-headers curl  
WORKDIR /root/build  
  
RUN git clone \--branch 2017.07 https://github.com/rakudo/rakudo.git \  
&& cd rakudo \  
&& perl Configure.pl --prefix=/usr/local \--backend=moar --gen-moar \  
&& make install  
  
RUN git clone \--branch v0.1.26 https://github.com/ugexe/zef.git \  
&& cd zef \  
&& perl6 -Ilib bin/zef install .  
  
ENV PATH=/usr/local/share/perl6/site/bin:$PATH  
RUN zef install "Bailador:ver<0.0.10>"  
  
WORKDIR /root  
RUN rm -rf build/ && apk del gcc musl-dev make linux-headers  
  
EXPOSE 3000  
ENTRYPOINT ["bailador"]  

