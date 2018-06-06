FROM purplekarrot/gcc-7:latest  
  
  
RUN true \  
&& apt-get -qq update \  
&& apt-get -qq install -y --no-install-recommends \  
python \  
lcov \  
gcovr \  
&& rm -rf /var/lib/apt/lists/*  
  
  
ENTRYPOINT []  

