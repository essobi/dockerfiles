# Alpine based stockfish container  
# https://github.com/lantonov/asmFish  
#  
FROM bitnami/minideb:stretch  
  
LABEL maintainer "Kayvan Sylvan <kayvansylvan@gmail.com>"  
  
ENV SOURCE_REPO https://github.com/lantonov/asmFish  
ENV VERSION master  
  
ADD ${SOURCE_REPO}/archive/${VERSION}.tar.gz /root  
WORKDIR /root  
  
RUN if [ ! -d asmFish-${VERSION} ]; then tar xvzf *.tar.gz; fi \  
&& cd asmFish-${VERSION} \  
&& dpkg --add-architecture i386 \  
&& install_packages libgcc1:i386 \  
&& ./fasmg "x86/fish.asm" "asmfish" -e 100 -i "VERSION_OS='L'" -i
"VERSION_POST = 'popcnt'" \  
&& cp asmfish /usr/local/bin \  
&& chmod +x /usr/local/bin/asmfish \  
&& cd .. && rm -rf asmFish-${VERSION} *.tar.gz  
  
ENTRYPOINT [ "/usr/local/bin/asmfish" ]  

