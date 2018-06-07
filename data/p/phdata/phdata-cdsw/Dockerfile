#  
# Licensed to the Apache Software Foundation (ASF) under one  
# or more contributor license agreements. See the NOTICE file  
# distributed with this work for additional information  
# regarding copyright ownership. The ASF licenses this file  
# to you under the Apache License, Version 2.0 (the  
# "License"); you may not use this file except in compliance  
# with the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing,  
# software distributed under the License is distributed on an  
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY  
# KIND, either express or implied. See the License for the  
# specific language governing permissions and limitations  
# under the License.  
FROM docker.repository.cloudera.com/cdsw/engine:4  
# Install kudu repo  
RUN curl -o /etc/apt/sources.list.d/cloudera.list
http://archive.cloudera.com/kudu/ubuntu/xenial/amd64/kudu/cloudera.list  
RUN ls -al /etc/apt/sources.list.d/  
RUN apt-get update  
RUN apt-get -y --allow-unauthenticated install libkuduclient0 libkuduclient-
dev  
  
# Install some prereqs  
RUN apt-get update && \  
apt-get install -y rpm2cpio curl sudo ksh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# compile and install unixODBC 2.3.4  
WORKDIR /tmp  
RUN curl -O http://www.unixodbc.org/unixODBC-2.3.4.tar.gz && tar -xz -f
/tmp/unixODBC-2.3.4.tar.gz  
WORKDIR /tmp/unixODBC-2.3.4  
RUN CPPFLAGS="-DSIZEOF_LONG_INT=8" ./configure --prefix=/usr
--libdir=/usr/lib64 --sysconfdir=/etc --enable-gui=no --enable-drivers=no
--enable-iconv --with-iconv-char-enc=UTF8 --with-iconv-ucode-enc=UTF16LE
--enable-stats=no 1> configure_std.log 2> configure_err.log && make 1>
make_std.log 2> make_err.log && make install 1> makeinstall_std.log 2>
makeinstall_err.log  
  
# install teradata drivers  
ADD tdicu1610_16.10.00.00-2_all.deb /tmp/tdicu1610_16.10.00.00-2_all.deb  
ADD tdodbc1610_16.10.00.02-2_all.deb /tmp/tdodbc1610_16.10.00.02-2_all.deb  
RUN dpkg -i /tmp/tdicu1610_16.10.00.00-2_all.deb  
# teradata odbc README file specifies running the tdodbc installer using the
korn shell:  
RUN /bin/ksh -c 'dpkg -i /tmp/tdodbc1610_16.10.00.02-2_all.deb'  
  
# create folders  
RUN mkdir /opt/teradata/client/ODBC_32 && mkdir /opt/teradata/client/ODBC_64  
  
# create symlinks  
RUN ln -s /opt/teradata/client/16.10/lib64 /opt/teradata/client/ODBC_64/lib &&
ln -s /opt/teradata/client/16.10/odbc_64/locale
/opt/teradata/client/ODBC_64/locale && ln -s
/opt/teradata/client/16.10/include /opt/teradata/client/ODBC_64/include && ln
-s /opt/teradata/client/16.10/lib /opt/teradata/client/ODBC_32/lib && ln -s
/opt/teradata/client/16.10/odbc_32/locale /opt/teradata/client/ODBC_32/locale
&& ln -s /opt/teradata/client/16.10/include
/opt/teradata/client/ODBC_32/include && ln -s
/opt/teradata/client/16.10/include /opt/teradata/client/16.10/odbc_64/include
&& ln -s /opt/teradata/client/16.10/lib64
/opt/teradata/client/16.10/odbc_64/lib && ln -s
/opt/teradata/client/16.10/include /opt/teradata/client/16.10/odbc_32/include
&& ln -s /opt/teradata/client/16.10/lib /opt/teradata/client/16.10/odbc_32/lib
&& ln -s /opt/teradata/client/16.10/lib/ivtrc27.so
/opt/teradata/client/16.10/lib/odbctrac.so && ln -s
/opt/teradata/client/16.10/lib64/ddtrc27.so
/opt/teradata/client/16.10/lib64/odbctrac.so && ln -s
/opt/teradata/client/16.10/etc/.ttupath_1610_bash.env
/opt/teradata/client/etc/ttu_bash.env && ln -s
/opt/teradata/client/16.10/etc/.ttupath_1610_csh.env
/opt/teradata/client/etc/ttu_csh.env && rm /usr/lib64/libodbcinst.so && ln -s
/opt/teradata/client/16.10/lib64/libodbcinst.so /usr/lib64/libodbcinst.so &&
rm /usr/lib64/libodbc.so && ln -s /opt/teradata/client/16.10/lib64/libodbc.so
/usr/lib64/libodbc.so  
  
# create environment variables  
ENV ODBCINI=/opt/teradata/client/16.10/odbc_64/odbc.ini  
ENV LD_LIBRARY_PATH=/opt/teradata/client/ODBC_64/lib:$LD_LIBRARY_PATH  
  
# create odbc files  
ADD etc_odbc.ini /etc/odbc.ini  
ADD 1610_odbc32_odbc.ini /opt/teradata/client/16.10/odbc_32/odbc.ini  
ADD 1610_odbc64_odbc.ini /opt/teradata/client/16.10/odbc_64/odbc.ini  
ADD odbc32_odbc.ini /opt/teradata/client/ODBC_32/odbc.ini  
ADD odbc64_odbc.ini /opt/teradata/client/ODBC_64/odbc.ini  
ADD etc_odbcinst.ini /etc/odbcinst.ini  
ADD 1610_odbc32_odbcinst.ini /opt/teradata/client/16.10/odbc_32/odbcinst.ini  
ADD 1610_odbc64_odbcinst.ini /opt/teradata/client/16.10/odbc_64/odbcinst.ini  
ADD odbc32_odbcinst.ini /opt/teradata/client/ODBC_32/odbcinst.ini  
ADD odbc64_odbcinst.ini /opt/teradata/client/ODBC_64/odbcinst.ini  
ADD genuine_TTU /opt/teradata/client/16.10/.genuine_TTU  
RUN touch /opt/teradata/client/16.10/ttu_softlinks_yes_1610 && touch
/opt/teradata/client/16.10/ttu_updateETC_1610  
RUN chmod 4111 /opt/teradata/client/16.10/.genuine_TTU  
  
# Give cdsw user sudo  
RUN echo "cdsw ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# install teradata python library  
#RUN pip2 install teradata  
#RUN pip3 install teradata  
# Install Oracle basic driver and odbc driver v12.2  
ADD instantclient-odbc-linux.x64-12.2.0.1.0.zip /tmp/instantclient-odbc-
linux.x64-12.2.0.1.0.zip  
ADD instantclient-basic-linux.x64-12.2.0.1.0.zip /tmp/instantclient-basic-
linux.x64-12.2.0.1.0.zip  
RUN unzip /tmp/instantclient-odbc-linux.x64-12.2.0.1.0.zip -d /opt/oracle/  
RUN unzip /tmp/instantclient-basic-linux.x64-12.2.0.1.0.zip -d /opt/oracle/  
RUN ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1
/opt/oracle/instantclient_12_2/libclntsh.so && ln -s
/opt/oracle/instantclient_12_2/libocci.so.12.1
/opt/oracle/instantclient_12_2/libocci.so  
RUN apt-get install libaio1  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_2:$LD_LIBRARY_PATH  
RUN /opt/oracle/instantclient_12_2/odbc_update_ini.sh /
/opt/oracle/instantclient_12_2 "Oracle 12c ODBC driver" OracleODBC-12c
/etc/odbc.ini  
  
# get maven 3.5.2  
RUN curl -o /tmp/apache-maven-3.5.2.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz  
  
# verify checksum  
RUN echo "948110de4aab290033c23bf4894f7d9a /tmp/apache-maven-3.5.2.tar.gz" |
md5sum -c  
  
# install maven  
RUN tar xzf /tmp/apache-maven-3.5.2.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.5.2 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.5.2.tar.gz  
ENV MAVEN_HOME /opt/maven  
  
# install nvidia drivers to support GPUs  
# from: https://www.cloudera.com/documentation/data-science-
workbench/latest/topics/cdsw_gpu.html#cdsw_gpu  
RUN
NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5
&& \  
NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80 && \  
apt-key adv --fetch-keys
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
&& \  
apt-key adv --export \--no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 >
cudasign.pub && \  
echo "$NVIDIA_GPGKEY_SUM cudasign.pub" | sha256sum -c --strict - && rm
cudasign.pub && \  
echo "deb
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" >
/etc/apt/sources.list.d/cuda.list  
  
ENV CUDA_VERSION 8.0.61  
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"  
  
ENV CUDA_PKG_VERSION 8-0=$CUDA_VERSION-1  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
cuda-nvgraph-$CUDA_PKG_VERSION \  
cuda-cusolver-$CUDA_PKG_VERSION \  
cuda-cublas-8-0=8.0.61.2-1 \  
cuda-cufft-$CUDA_PKG_VERSION \  
cuda-curand-$CUDA_PKG_VERSION \  
cuda-cusparse-$CUDA_PKG_VERSION \  
cuda-npp-$CUDA_PKG_VERSION \  
cuda-cudart-$CUDA_PKG_VERSION && \  
ln -s cuda-8.0 /usr/local/cuda && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
RUN echo "deb http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list  
  
ENV CUDNN_VERSION 6.0.21  
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libcudnn6=$CUDNN_VERSION-1+cuda8.0 && \  
rm -rf /var/lib/apt/lists/*  
  
# get protoc 3.3.0  
WORKDIR /tmp  
RUN curl -OL
https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip  
RUN unzip /tmp/protoc-3.3.0-linux-x86_64.zip -d /tmp/protoc3  
  
# move protoc to /usr/local/bin/ and /usr/local/include  
RUN mv /tmp/protoc3/bin/* /usr/local/bin/  
RUN mv protoc3/include/* /usr/local/include/  

