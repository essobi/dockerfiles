#Image: gzynda/tacc-maverick-cuda8  
#Version: 0.0.1  
  
FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04  
  
########################################  
# Configure ENV  
########################################  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
########################################  
# Add docker-clean  
########################################  
  
RUN echo "#!/bin/bash\n\  
apt-get clean\n\  
[ -x \"\$(command -v conda)\" ] && conda clean -tipsy\n\  
for dir in /tmp/* /var/tmp/* /home/jupyter/{.ccache,.cache/pip,conda-
bld,.conda} /root/* /root/\\.[^\\.]* /var/lib/apt/lists/* /var/log/*; do\n\  
[ -e \$dir ] && rm -rf \$dir || true\n\  
done" > /usr/bin/docker-clean && chmod a+rx /usr/bin/docker-clean && docker-
clean  
  
########################################  
# Add mount points  
########################################  
  
RUN mkdir /scratch /work /home1 /gpfs /corral-repl /corral-tacc /data  
  
########################################  
# Install mpi  
########################################  
  
# necessities and IB stack  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends \  
curl vim-nox gfortran bison libibverbs-dev libibmad-dev libibumad-dev
librdmacm-dev libmlx5-dev libmlx4-dev && \  
docker-clean  
  
# Install mvapich2-2.2  
ARG MAJV=2  
ARG MINV=2  
ARG DIR=mvapich${MAJV}-${MAJV}.${MINV}  
  
RUN curl http://mvapich.cse.ohio-
state.edu/download/mvapich/mv${MAJV}/${DIR}.tar.gz | tar -xzf - \  
&& cd ${DIR} \  
&& ./configure \  
&& make -j $(nproc --all 2>/dev/null || echo 2) && make install \  
&& mpicc examples/hellow.c -o /usr/bin/hellow \  
&& cd ../ && rm -rf ${DIR}  

