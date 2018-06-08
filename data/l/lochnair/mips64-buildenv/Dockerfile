FROM lochnair/buildenv-base:alpine  
  
LABEL Description="musl build environment for MIPS64"  
LABEL Maintainer="Nils Andreas Svee <me@lochnair.net>"  
  
ARG BINUTILS_VER=2.29  
ARG GCC_VER=7.2.0  
ARG GMP_VER=6.1.2  
ARG ISL_VER=0.18  
ARG KERNEL_VER=4.13.2  
ARG MPC_VER=1.0.3  
ARG MPFR_VER=3.1.5  
ARG MUSL_VER=1.1.16  
ENV PATH="/opt/cross/bin:${PATH}"  
COPY root/ /  
  
RUN /build_toolchain.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

