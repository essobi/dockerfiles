FROM tensorflow/tensorflow:1.3.0-rc1-py3  
ARG USERNAME  
ARG PASSWORD  
  
###############################  
### Bazel ###  
###############################  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
vim \  
wget \  
openjdk-8-jdk  
  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list \  
&& curl https://bazel.build/bazel-release.pub.gpg | apt-key add -  
  
RUN apt-get update \  
&& apt-get install -y bazel \  
&& rm -rf /var/lib/apt/lists/*  
  
###############################  
### workspace ###  
###############################  
RUN mkdir -p /usr/src/facets  
ENV WORKSPACE /usr/src/facets  
WORKDIR /usr/src/facets  
  
ARG FACETS_VER=unknown  
  
##############################  
### facets source ###  
##############################  
RUN FACETS_VER=${FACETS_VER} git clone
https://$USERNAME:$PASSWORD@github.com/PAIR-code/facets.git .  
  
##############################  
### facets visualization ###  
##############################  
RUN bazel build facets:facets_jupyter  
RUN jupyter nbextension install facets-dist/  
  
##############################  
### facets visualization ###  
##############################  
EXPOSE 6006  
RUN bazel build facets_dive/demo  
  

