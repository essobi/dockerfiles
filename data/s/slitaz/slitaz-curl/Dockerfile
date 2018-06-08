FROM slitaz/slitaz-base:2.19  
  
COPY *.tazpkg /  
  
RUN tazpkg -i zlib-1.2.8-x86_64.tazpkg && \  
tazpkg -i libidn-1.21-x86_64.tazpkg && \  
tazpkg -i pcre-8.39-x86_64.tazpkg && \  
tazpkg -i libcrypto-1.0.1q-x86_64.tazpkg && \  
tazpkg -i libssl-1.0.1q-x86_64.tazpkg && \  
tazpkg -i libcurl-7.40.0-x86_64.tazpkg && \  
tazpkg -i grep-2.25-x86_64.tazpkg && \  
tazpkg -i curl-7.40.0-x86_64.tazpkg && \  
rm /*.tazpkg  

