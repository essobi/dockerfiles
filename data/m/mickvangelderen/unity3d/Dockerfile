FROM ubuntu:devel  
  
RUN apt-get update && apt-get install --yes curl xvfb  
  
RUN curl --output "/tmp/unity.deb"
"http://beta.unity3d.com/download/061bcf22327f/unity-
editor_amd64-2017.1.0xf3Linux.deb"  
RUN apt-get install --yes "/tmp/unity.deb" \  
&& rm --force "/tmp/unity.deb"  

