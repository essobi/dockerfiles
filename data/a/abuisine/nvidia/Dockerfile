FROM ubuntu:17.10  
  
ENV NVIDIA_DRIVER_VERSION=375.66  
  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>" \  
com.prometheus.monitoring="true" \  
com.prometheus.port="9090" \  
version="${NVIDIA_DRIVER_VERSION}-7"  
# install python modules for monitoring  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \  
&& apt-get install -yqq --no-install-recommends \  
python \  
python-pip \  
python-wheel \  
python-setuptools \  
&& pip install nvidia-ml-py \  
&& pip install prometheus_client \  
&& apt-get -yqq remove --purge python-pip \  
&& apt-get -yqq autoremove --purge \  
&& apt-get -yqq clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY resources/${NVIDIA_DRIVER_VERSION}/etc/OpenCL/vendors/nvidia.icd
/etc/OpenCL/vendors/nvidia.icd  
COPY resources/${NVIDIA_DRIVER_VERSION}/usr/bin/nvidia-smi /usr/bin/  
COPY resources/${NVIDIA_DRIVER_VERSION}/usr/share/nvidia/nvidia-application-
profiles-${NVIDIA_DRIVER_VERSION}-rc /usr/share/nvidia/nvidia-application-
profiles-${NVIDIA_DRIVER_VERSION}-rc  
COPY resources/${NVIDIA_DRIVER_VERSION}/usr/lib/x86_64-linux-
gnu/libcuda.so.${NVIDIA_DRIVER_VERSION} \  
resources/${NVIDIA_DRIVER_VERSION}/usr/lib/x86_64-linux-gnu/libnvidia-
fatbinaryloader.so.${NVIDIA_DRIVER_VERSION} \  
resources/${NVIDIA_DRIVER_VERSION}/usr/lib/x86_64-linux-gnu/libnvidia-
opencl.so.${NVIDIA_DRIVER_VERSION} \  
resources/${NVIDIA_DRIVER_VERSION}/usr/lib/x86_64-linux-gnu/libOpenCL.so.1.0.0
\  
resources/${NVIDIA_DRIVER_VERSION}/usr/lib/x86_64-linux-gnu/libnvidia-
ml.so.${NVIDIA_DRIVER_VERSION} \  
resources/${NVIDIA_DRIVER_VERSION}/usr/lib/x86_64-linux-gnu/libnvidia-
ptxjitcompiler.so.${NVIDIA_DRIVER_VERSION} \  
/usr/lib/x86_64-linux-gnu/  
  
COPY resources/docker-entrypoint.py \  
resources/NVMLCollector.py \  
/usr/local/bin/  
  
RUN chmod +x /usr/local/bin/docker-entrypoint.py /usr/bin/nvidia-smi  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libcuda.so.${NVIDIA_DRIVER_VERSION}
/usr/lib/x86_64-linux-gnu/libcuda.so.1 \  
&& ln -s /usr/lib/x86_64-linux-gnu/libnvidia-
opencl.so.${NVIDIA_DRIVER_VERSION} /usr/lib/x86_64-linux-gnu/libnvidia-
opencl.so.1 \  
&& ln -s /usr/lib/x86_64-linux-gnu/libnvidia-ml.so.${NVIDIA_DRIVER_VERSION}
/usr/lib/x86_64-linux-gnu/libnvidia-ml.so.1 \  
&& ln -s /usr/lib/x86_64-linux-gnu/libnvidia-ml.so.1 /usr/lib/x86_64-linux-
gnu/libnvidia-ml.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/libOpenCL.so.1.0.0 /usr/lib/x86_64-linux-
gnu/libOpenCL.so.1.0 \  
&& ln -s /usr/lib/x86_64-linux-gnu/libOpenCL.so.1.0 /usr/lib/x86_64-linux-
gnu/libOpenCL.so.1 \  
&& ln -s /usr/lib/x86_64-linux-gnu/libOpenCL.so.1 /usr/lib/x86_64-linux-
gnu/libOpenCL.so \  
&& ldconfig  
  
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.py" ]  
CMD [ "--collector-port", "9090" ]

