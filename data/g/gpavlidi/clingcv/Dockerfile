FROM gpavlidi/cling  
MAINTAINER Yanis Pavlidis <yanis@pavlidis.email>  
  
RUN apt-get update \  
&& apt-get install -y libopencv-dev --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG en-US  
  
# if i wasnt caring about user input params i d use the below entrypoint.  
# problem is that user cannot pass the $() shell substitution  
#ENTRYPOINT cling -Wc++11-extensions -std=c++11 -liostream -lvector -lstring
-lunordered_map -lqueue -lstack -lalgorithm -lopencv2/opencv.hpp
-L/usr/lib/x86_64-linux-gnu/ $(pkg-config --libs-only-l opencv)  
ENTRYPOINT ["cling"]

