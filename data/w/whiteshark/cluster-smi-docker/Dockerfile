FROM nvidia/cuda:9.0-devel-ubuntu16.04  
LABEL maintainer="ivan.eggel@gmail.com"  
  
# Install necessary packages  
# ***************************************  
RUN apt-get update && apt-get install -y \  
wget \  
libtool-bin \  
autoconf \  
g++ \  
make \  
git \  
golang-go  
  
# Download and compile zermomq (dependency)  
# ***************************************  
RUN mkdir /zmq  
RUN wget http://files.patwie.com/mirror/zeromq-4.1.0-rc1.tar.gz  
RUN tar -xf zeromq-4.1.0-rc1.tar.gz -C /zmq  
WORKDIR /zmq/zeromq-4.1.0  
RUN ./autogen.sh  
RUN ./configure  
RUN ./configure --prefix=/zmq/zeromq-4.1.0/dist  
RUN make  
RUN make install  
  
# Download cluster-smi code  
# ***************************************  
WORKDIR /gocode/src/github.com/patwie  
RUN git clone https://github.com/PatWie/cluster-smi.git  
  
# Adjust workdir to base code dir  
#***************************************  
WORKDIR cluster-smi  
  
# Set all necessary environment variables  
# ***************************************  
ENV PKG_CONFIG_PATH="/zmq/zeromq-4.1.0/dist/lib/pkgconfig:${PKG_CONFIG_PATH}"  
ENV LD_LIBRARY_PATH="/zmq/zeromq-4.1.0/dist/lib:${LD_LIBRARY_PATH}"  
ENV GOPATH="/gocode"  
#Location of yaml config file inside container  
ENV CLUSTER_SMI_CONFIG_PATH="/cluster-smi.yml"  
#Create new mandatory config file with default values  
# ***************************************  
RUN cp config.example.go config.go  
# Sidenote: At runtime, the default default should be replaced, use: "docker
run -v <local-path-of-yml-config>:/cluster-smi.yml ..."  
# Set CFLAGS and LDFLAGS according to CUDA setup before compilation  
# ***************************************  
RUN sed -i 's/#cgo CFLAGS:
-I\/graphics\/opt\/opt_Ubuntu16.04\/cuda\/toolkit_8.0\/cuda\/include/#cgo
CFLAGS: -I\/usr\/local\/cuda\/include/g' ./nvml/nvml.go  
RUN sed -i 's/#cgo LDFLAGS: -lnvidia-ml
-L\/graphics\/opt\/opt_Ubuntu16.04\/cuda\/toolkit_8.0\/cuda\/lib64\/stubs/#cgo
LDFLAGS: -lnvidia-ml
-L\/usr\/local\/cuda\/targets\/x86_64-linux\/lib\/stubs/g' ./nvml/nvml.go  
  
# BUILD cluster-smi  
# ***************************************  
RUN cd proc && go install  
RUN make all  
  

