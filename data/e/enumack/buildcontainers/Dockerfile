FROM gcc:8.1  
LABEL maintainer="loligothick@gmail.com"  
  
RUN apt -qq update \  
&& apt -qq install -y cmake --no-install-recommends \  
&& apt -qq purge --auto-remove -y git \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CC="gcc" \  
CXX="g++" \  
COVERAGE_COMMAND="/usr/bin/gcov-7" \  
COVERAGE_FLAGS="--coverage"

