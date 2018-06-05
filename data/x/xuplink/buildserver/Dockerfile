FROM buildpack-deps:artful-scm  
  
ADD https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg
/tmp/bazel.pub.gpg  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list && \  
apt-key add /tmp/bazel.pub.gpg  
RUN apt-get update && apt-get install -y bazel \  
&& rm -rf /var/lib/apt/lists/*

