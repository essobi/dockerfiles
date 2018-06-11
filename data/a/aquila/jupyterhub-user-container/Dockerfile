# Run with the DockerSpawner in JupyterHub  
FROM jupyterhub/singleuser  
  
MAINTAINER Andreas Lang <andreas.lang@aquilainsight.com>  
  
ENV PIP2=pip2 \  
PIP3=$CONDA_DIR/bin/pip \  
SPARK_HOME='/opt/spark' \  
SPARK_OPTS='--master=sparkmaster:7077' \  
SCALA_VERSION='2.11.8' \  
SCALA_HOME="/opt/scala/scala-${SCALA_VERSION}" \  
TORNADO_VERSION=4.5.3 \  
JUPYTERHUB_VERSION=0.8.1  
# The following four lines are introduced to skip jupyterhub/singleuser which
seems to miss updates  
USER root  
WORKDIR /home  
RUN userdel jovyan && rm -rf /home/jovyan  
ENV SHELL /bin/bash  
  
RUN apt-get update && apt-get install -y \  
python-pip \  
curl \  
cmake \  
language-pack-en \  
libsasl2-2 \  
libsasl2-modules-gssapi-mit \  
libopencv-dev \  
python-opencv \  
freetds-dev \  
libsasl2-dev \  
openjdk-8-jdk \  
git \  
tar \  
libssl-dev \  
unzip \  
&& update-locale LANG=en_GB.UTF-8 LC_MESSAGES=POSIX \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/scala \  
&& cd /opt/scala \  
&& curl
https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz
| tar xvfz -  
  
COPY python_libraries .  
# install packages not provided by ubuntu  
RUN $PIP2 install --upgrade pip \  
&& $PIP2 install --upgrade $(paste -s -d ' ' python_libraries) \  
&& $PIP3 install --upgrade pip \  
&& $PIP3 install --upgrade $(paste -s -d ' ' python_libraries) \  
jupyterhub==${JUPYTERHUB_VERSION} \  
tornado==${TORNADO_VERSION}  
  
# Use a patched version of PyHive to allow spark connections  
RUN $PIP2 install --upgrade
https://github.com/andreaslang/PyHive/archive/SparkHiveThriftServerDialect.zip  
RUN $PIP3 install --upgrade
https://github.com/andreaslang/PyHive/archive/SparkHiveThriftServerDialect.zip  
  
WORKDIR /  
ENV OPENCV_VERSION="3.4.1"  
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \  
&& unzip ${OPENCV_VERSION}.zip \  
&& mkdir /opencv-${OPENCV_VERSION}/cmake_binary \  
&& cd /opencv-${OPENCV_VERSION}/cmake_binary \  
&& cmake -DBUILD_TIFF=ON \  
-DBUILD_opencv_java=OFF \  
-DWITH_CUDA=OFF \  
-DENABLE_AVX=ON \  
-DWITH_OPENGL=ON \  
-DWITH_OPENCL=ON \  
-DWITH_IPP=ON \  
-DWITH_TBB=ON \  
-DWITH_EIGEN=ON \  
-DWITH_V4L=ON \  
-DBUILD_TESTS=OFF \  
-DBUILD_PERF_TESTS=OFF \  
-DCMAKE_BUILD_TYPE=RELEASE \  
-DCMAKE_INSTALL_PREFIX=$(python3.6 -c "import sys; print(sys.prefix)") \  
-DPYTHON_EXECUTABLE=$(which python3.6) \  
-DPYTHON_INCLUDE_DIR=$(python3.6 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \  
-DPYTHON_PACKAGES_PATH=$(python3.6 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \  
&& make install \  
&& rm /${OPENCV_VERSION}.zip \  
&& rm -r /opencv-${OPENCV_VERSION}  
  
COPY .pgpass /etc/skel/.pgpass  
COPY .ipython /etc/skel/.ipython  
COPY *.ipynb /examples/  
RUN chmod 600 /etc/skel/.pgpass \  
&& ln -s /media media \  
&& ln -s /examples examples  
  
COPY spark ${SPARK_HOME}  
# need to fix a few things before exposing toree  
#RUN jupyter toree install --spark_home="${SPARK_HOME}"
--interpreters="Scala,PySpark,SQL"  
RUN python2 -m pip install --upgrade ipython==5.5.0 ipykernel && python2 -m
ipykernel install  
  
EXPOSE 8888  
WORKDIR /srv/singleuser  
  
ADD systemuser.sh /srv/singleuser/systemuser.sh  
CMD ["sh", "/srv/singleuser/systemuser.sh"]  

