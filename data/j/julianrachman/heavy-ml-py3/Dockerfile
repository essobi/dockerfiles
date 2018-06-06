FROM ubuntu:16.04  
MAINTAINER Julian Rachman <jmrachman@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
git \  
libcurl3-dev \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
openjdk-8-jdk \  
openjdk-8-jre-headless \  
pkg-config \  
python \  
python3 \  
python-dev \  
python3-dev \  
python3-tk \  
python3-wheel \  
rsync \  
software-properties-common \  
unzip \  
vim \  
wget \  
zip \  
zlib1g-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
  
RUN pip --no-cache-dir install \  
GitPython \  
Pillow \  
beautifulsoup4 \  
elasticsearch \  
h5py \  
ipykernel \  
jupyter \  
jupyter-cjk-xelatex \  
matplotlib \  
nbconvert \  
numpy \  
pandas \  
requests \  
scipy \  
scrapy \  
selenium \  
sklearn \  
zeep \  
&& \  
python3 -m ipykernel.kernelspec  
  
#========================#  
# Firefox and Geckodriver  
#========================#  
ARG FIREFOX_VERSION=54.0  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
ARG GECKODRIVER_VERSION=0.17.0  
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& rm -rf /opt/geckodriver \  
&& tar -C /opt -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \  
&& chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver  
  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
COPY notebooks /notebooks  
  
COPY run_jupyter.sh /notebooks/config  
  
EXPOSE 6006  
EXPOSE 8888  
WORKDIR "/notebooks"  
  
RUN cd config && chmod +x run_jupyter.sh  
  
# Set up Bazel.  
# Running bazel inside a `docker build` command causes trouble, cf:  
# https://github.com/bazelbuild/bazel/issues/134  
# The easiest solution is to set up a bazelrc file forcing --batch.  
RUN echo "startup --batch" >>/etc/bazel.bazelrc  
# Similarly, we need to workaround sandboxing issues:  
# https://github.com/bazelbuild/bazel/issues/418  
RUN echo "build --spawn_strategy=standalone --genrule_strategy=standalone" \  
>>/etc/bazel.bazelrc  
# Install the most recent bazel release.  
ENV BAZEL_VERSION 0.5.0  
WORKDIR /  
RUN mkdir /bazel && \  
cd /bazel && \  
curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -O
https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-
installer-linux-x86_64.sh && \  
curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -o
/bazel/LICENSE.txt
https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE && \  
chmod +x bazel-*.sh && \  
./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \  
cd / && \  
rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh  
  
# Download and build TensorFlow.  
RUN git clone https://github.com/tensorflow/tensorflow.git && \  
cd tensorflow && \  
git checkout r1.3  
WORKDIR /tensorflow  
  
# TODO(craigcitro): Don't install the pip package, since it makes it  
# more difficult to experiment with local changes. Instead, just add  
# the built directory to the path.  
ENV CI_BUILD_PYTHON python3  
  
RUN tensorflow/tools/ci_build/builds/configured CPU \  
bazel build -c opt --copt=-mavx --copt=-mavx2 --copt=-mfma
--copt=-mfpmath=both --copt=-msse4.2 --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" \  
tensorflow/tools/pip_package:build_pip_package && \  
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip && \  
pip --no-cache-dir install --upgrade /tmp/pip/tensorflow-*.whl && \  
rm -rf /tmp/pip && \  
rm -rf /root/.cache  
# Clean up pip wheel and Bazel cache when done.  
WORKDIR /  
CMD ["/bin/bash"]  

