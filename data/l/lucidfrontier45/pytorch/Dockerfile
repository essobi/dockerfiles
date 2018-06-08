FROM lucidfrontier45/miniconda:xenial-cuda-base  
  
ENV PYTORCH_VERSION 0.4  
  
RUN set -ex \  
&& pkgs=" \  
pytorch=${PYTORCH_VERSION} \  
torchvision \  
" \  
&& conda install -y ${pkgs} -c pytorch \  
&& conda clean -i -l -t -y

