FROM vishnumohan/tensorflow-dcos  
  
ARG CONDA_ENV_YML="tensorflow-root-conda-cudnn-env.yml"  
ARG NVIDIA_CUDA_MAJOR_VERSION="9-0"  
ARG NVIDIA_CUDA_PKG_VERSION="9.0.176-1"  
ARG NVIDIA_CUDA_VERSION="9.0"  
ARG NVIDIA_CUDA_TOOLS_GPG_KEY="7fa2af80"  
ARG NVIDIA_CUDNN_MAJOR_VERSION="7"  
ARG NVIDIA_CUDNN_PKG_VERSION="7.1.1.5-1+cuda9.0"  
ARG NVIDIA_DISTRO="ubuntu1604"  
ARG NVIDIA_DRIVER_CAPABILITIES="compute,utility"  
ARG NVIDIA_NCCL_MAJOR_VERSION="2"  
ARG NVIDIA_NCCL_PKG_VERSION="2.1.2-1+cuda9.0"  
ARG NVIDIA_REQUIRE_CUDA="cuda>=9.0"  
ARG NVIDIA_URL="http://developer.download.nvidia.com/compute"  
ARG NVIDIA_VISIBLE_DEVICES="all"  
ARG NVIDIA_VOLUMES_NEEDED="nvidia_driver"  
ARG
TENSORFLOW_JNI_SHA256="e657b0966c963cb9a0e5ff42917b589268b361bf463604c34e5fcf85ac87007e"  
ARG TENSORFLOW_URL="https://storage.googleapis.com/tensorflow"  
ARG TENSORFLOW_VARIANT="gpu"  
ARG TENSORFLOW_VERSION="1.8.0"  
LABEL com.nvidia.volumes.needed=${NVIDIA_VOLUMES_NEEDED:-"nvidia_driver"} \  
com.nvidia.cuda.version="${NVIDIA_CUDA_PKG_VERSION}" \  
com.nvidia.cudnn.version="${NVIDIA_CUDNN_VERSION}"  
  
# Need to unset LD_LIBRARY_PATH first so that libraries in
${MESOSPHERE_PREFIX}/libmesos-bundle/lib don't interfere with apt  
RUN unset LD_LIBRARY_PATH \  
&& apt-key adv --keyserver "${GPG_KEYSERVER}" \--recv-keys
"${NVIDIA_CUDA_TOOLS_GPG_KEY}" \  
&& echo "deb ${NVIDIA_URL}/cuda/repos/${NVIDIA_DISTRO}/x86_64 /" >
/etc/apt/sources.list.d/nvidia-cuda.list \  
&& echo "deb ${NVIDIA_URL}/machine-learning/repos/${NVIDIA_DISTRO}/x86_64 /" >
/etc/apt/sources.list.d/nvidia-ml.list \  
&& apt-get update -yq --fix-missing \  
&& apt-get install -yq --no-install-recommends \  
"cuda-cudart-${NVIDIA_CUDA_MAJOR_VERSION}=${NVIDIA_CUDA_PKG_VERSION}" \  
"cuda-libraries-${NVIDIA_CUDA_MAJOR_VERSION}=${NVIDIA_CUDA_PKG_VERSION}" \  
"cuda-libraries-dev-${NVIDIA_CUDA_MAJOR_VERSION}=${NVIDIA_CUDA_PKG_VERSION}" \  
"libnccl${NVIDIA_NCCL_MAJOR_VERSION}=${NVIDIA_NCCL_PKG_VERSION}" \  
"libcudnn${NVIDIA_CUDNN_MAJOR_VERSION}=${NVIDIA_CUDNN_PKG_VERSION}" \  
&& cd /usr/local \  
&& ln -s "cuda-${NVIDIA_CUDA_VERSION}" cuda \  
&& cd cuda-"${NVIDIA_CUDA_VERSION}/targets/x86_64-linux/lib" \  
&& ln -s stubs/libcuda.so libcuda.so.1 \  
&& echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf \  
&& echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf \  
&& curl --retry 3 -fsSL -O
"${TENSORFLOW_URL}/libtensorflow/libtensorflow_jni-${TENSORFLOW_VARIANT}-linux-x86_64-${TENSORFLOW_VERSION}.tar.gz"
\  
&& echo "${TENSORFLOW_JNI_SHA256}"
"libtensorflow_jni-${TENSORFLOW_VARIANT}-linux-x86_64-${TENSORFLOW_VERSION}.tar.gz"
| sha256sum -c - \  
&& tar xf
"libtensorflow_jni-${TENSORFLOW_VARIANT}-linux-x86_64-${TENSORFLOW_VERSION}.tar.gz"
"./libtensorflow_jni.so" \  
&& mv "libtensorflow_jni.so" "/usr/local/lib" \  
&& rm
"libtensorflow_jni-${TENSORFLOW_VARIANT}-linux-x86_64-${TENSORFLOW_VERSION}.tar.gz"
\  
&& rm /usr/lib/x86_64-linux-gnu/libcurl.so.4 \  
&& cp "${MESOSPHERE_PREFIX}/libmesos-bundle/lib/libcurl.so.4"
/usr/lib/x86_64-linux-gnu/libcurl.so.4.4.0 \  
&& ln -s /usr/lib/x86_64-linux-gnu/libcurl.so.4.4.0 /usr/lib/x86_64-linux-
gnu/libcurl.so.4 \  
&& ldconfig \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY "${CONDA_ENV_YML}" "${CONDA_DIR}/"  
  
RUN ${CONDA_DIR}/bin/conda env update --json -q -f
"${CONDA_DIR}/${CONDA_ENV_YML}" \  
&& ${CONDA_DIR}/bin/conda update --json --all -yq \  
&& ${CONDA_DIR}/bin/conda clean --json -tipsy \  
&& rm -rf "${HOME}/.cache/pip" "${HOME}/.cache/yarn" "${HOME}/.node-gyp"  
  
ENV NVIDIA_VISIBLE_DEVICES=${NVIDIA_VISIBLE_DEVICES:-"all"} \  
NVIDIA_DRIVER_CAPABILITIES=${NVIDIA_DRIVER_CAPABILITIES:-"compute,utility"} \  
NVIDIA_REQUIRE_CUDA=${NVIDIA_REQUIRE_CUDA:-"cuda>=9.0"} \  
PATH="/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}" \  
LD_LIBRARY_PATH="/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}"  

