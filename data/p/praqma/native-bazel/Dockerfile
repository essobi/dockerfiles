FROM openjdk:8  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" \  
| tee /etc/apt/sources.list.d/bazel.list  
  
RUN curl \  
\--silent \  
\--location \  
https://bazel.build/bazel-release.pub.gpg \  
\--output /tmp/bazel-release.pub.gpg \  
&& apt-key add /tmp/bazel-release.pub.gpg  
  
RUN apt-get update \  
&& apt-get install --yes \  
build-essential \  
bazel \  
graphviz  
  
# RUN cd ${HOME} \  
# && wget --quiet
https://github.com/bazelbuild/bazel/releases/download/0.5.4/bazel-0.5.4-installer-
linux-x86_64.sh \  
# && chmod +x bazel-0.5.4-installer-linux-x86_64.sh \  
# && ./bazel-0.5.4-installer-linux-x86_64.sh --user \  
# && ln -s ${HOME}/bin/bazel /usr/local/bin/bazel  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  

