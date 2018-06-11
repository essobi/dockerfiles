FROM alpine:3.7  
# Based on https://github.com/tatsushid/docker-alpine-py3-tensorflow-
jupyter/blob/master/Dockerfile  
# Changes:  
# - Bumping versions of Bazel and Tensorflow  
# - Add -Xmx to the Java params when building Bazel  
# - Disable TF_GENERATE_BACKTRACE and TF_GENERATE_STACKTRACE  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV LOCAL_RESOURCES 2048,.5,1.0  
ENV BAZEL_VERSION 0.10.0  
ENV TENSORFLOW_VERSION 1.8.0  
RUN apk add --update --no-cache ca-certificates wget python python2-tkinter
py-numpy py2-numpy-f2py freetype libpng libjpeg-turbo imagemagick graphviz git  
RUN apk add --no-cache --virtual=.build-deps \  
bash \  
cmake \  
curl \  
freetype-dev \  
g++ \  
libjpeg-turbo-dev \  
libpng-dev \  
linux-headers \  
make \  
musl-dev \  
openblas-dev \  
openjdk8 \  
patch \  
perl \  
python-dev \  
py-numpy-dev \  
py-pip \  
rsync \  
sed \  
swig \  
zip \  
&& cd /tmp \  
&& pip install -U pip setuptools wheel \  
&& pip install enum  
# && $(cd /usr/bin && ln -s python3 python)  
# Experimental...? Taken from https://github.com/sgerrand/alpine-pkg-glibc  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub  
RUN cd /tmp \  
&& curl -SLO https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-2.27-r0.apk \  
&& apk add glibc-2.27-r0.apk  
RUN cd /tmp \  
&& curl -SLO https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-bin-2.27-r0.apk \  
&& apk add glibc-bin-2.27-r0.apk  
RUN cd /tmp \  
&& curl -SLO https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-i18n-2.27-r0.apk \  
&& apk add glibc-i18n-2.27-r0.apk  
RUN /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8  
  
# Bazel download  
RUN curl -SLO
https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-dist.zip
\  
&& mkdir bazel-${BAZEL_VERSION} \  
&& unzip -qd bazel-${BAZEL_VERSION} bazel-${BAZEL_VERSION}-dist.zip  
  
# Bazel build and install  
RUN cd bazel-${BAZEL_VERSION} \  
&& sed -i -e 's/-classpath/-J-Xmx8192m -J-Xms128m -classpath/g'
scripts/bootstrap/compile.sh \  
&& bash compile.sh \  
&& cp -p output/bazel /usr/bin/  
  
# Tensorflow download  
RUN cd /tmp \  
&& curl -SL
https://github.com/tensorflow/tensorflow/archive/v${TENSORFLOW_VERSION}.tar.gz
\  
| tar xzf -  
  
# Tensorflow build  
RUN cd /tmp/tensorflow-${TENSORFLOW_VERSION} \  
&& : musl-libc does not have "secure_getenv" function \  
&& sed -i -e '/JEMALLOC_HAVE_SECURE_GETENV/d' third_party/jemalloc.BUILD \  
&& sed -i -e '/define TF_GENERATE_BACKTRACE/d'
tensorflow/core/platform/default/stacktrace.h \  
&& sed -i -e '/define TF_GENERATE_STACKTRACE/d'
tensorflow/core/platform/stacktrace_handler.cc \  
&& PYTHON_BIN_PATH=/usr/bin/python \  
PYTHON_LIB_PATH=/usr/lib/python2.7/site-packages \  
CC_OPT_FLAGS="-march=native" \  
TF_NEED_JEMALLOC=1 \  
TF_NEED_GCP=0 \  
TF_NEED_HDFS=0 \  
TF_NEED_S3=0 \  
TF_ENABLE_XLA=0 \  
TF_NEED_GDR=0 \  
TF_NEED_VERBS=0 \  
TF_NEED_OPENCL=0 \  
TF_NEED_CUDA=0 \  
TF_NEED_MPI=0 \  
bash configure  
RUN cd /tmp/tensorflow-${TENSORFLOW_VERSION} \  
&& bazel build -c opt --local_resources ${LOCAL_RESOURCES}
//tensorflow/tools/pip_package:build_pip_package  
RUN cd /tmp/tensorflow-${TENSORFLOW_VERSION} \  
&& ./bazel-bin/tensorflow/tools/pip_package/build_pip_package
/tmp/tensorflow_pkg  
RUN cp
/tmp/tensorflow_pkg/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl
/root  
  
# Tensorflow install to make sure it was build correctly  
RUN pip install --no-cache-dir
/root/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl \  
&& python -c 'import tensorflow'  

