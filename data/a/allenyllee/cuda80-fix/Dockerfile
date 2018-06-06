# cuda80-fix  
#  
# VERSION 0.0.1  
  
FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04  
LABEL maintainer="allen7575@gmail.com"  
  
##  
## Ubuntu - Packages - Search  
##
https://packages.ubuntu.com/search?suite=xenial&section=all&arch=amd64&searchon=contents&keywords=Search  
##  
  
############  
# update package list  
############  
RUN apt update  
  
###  
### solve for  
### >>> WARNING - libGL.so not found, refer to CUDA Getting Started Guide for
how to find and install them. <<<  
### >>> WARNING - libX11.so not found, refer to CUDA Getting Started Guide for
how to find and install them. <<<  
### >>> WARNING - Xlib.h not found, refer to CUDA Getting Started Guide for
how to find and install them. <<<  
### >>> WARNING - gl.h not found, refer to CUDA Getting Started Guide for how
to find and install them. <<<  
###  
### 2_Graphics/volumeFiltering  
### 2_Graphics/simpleGL  
### 2_Graphics/bindlessTexture  
### 2_Graphics/volumeRender  
### 2_Graphics/Mandelbrot  
### 2_Graphics/marchingCubes  
### 2_Graphics/simpleTexture3D  
### 3_Imaging/imageDenoising  
### 3_Imaging/recursiveGaussian  
### 3_Imaging/simpleCUDA2GL  
### 3_Imaging/postProcessGL  
### 3_Imaging/bicubicTexture  
### 3_Imaging/boxFilter  
### 3_Imaging/SobelFilter  
### 3_Imaging/cudaDecodeGL  
### 3_Imaging/bilateralFilter  
### 5_Simulations/particles  
### 5_Simulations/smokeParticles  
### 5_Simulations/oceanFFT  
### 5_Simulations/fluidsGL  
### 5_Simulations/nbody  
### 6_Advanced/FunctionPointers  
### 7_CUDALibraries/randomFog  
###  
RUN apt install -y libgl1-mesa-dev  
  
###  
### solve for  
### >>> WARNING - libGLU.so not found, refer to CUDA Getting Started Guide for
how to find and install them. <<<  
### >>> WARNING - glu.h not found, refer to CUDA Getting Started Guide for how
to find and install them. <<<  
###  
RUN apt install -y libglu1-mesa-dev  
  
###  
### solve for  
### /usr/bin/ld: cannot find -lglut  
### https://stackoverflow.com/questions/15064159/usr-bin-ld-cannot-find-lglut  
###  
RUN apt install -y freeglut3-dev  
  
###  
### solve for  
### >>> WARNING - egl.h not found, please install egl.h <<<  
### >>> WARNING - eglext.h not found, please install eglext.h <<<  
### >>> WARNING - gl31.h not found, please install gl31.h <<<  
###  
### 2_Graphics/simpleGLES_EGLOutput  
### 2_Graphics/simpleGLES  
### 2_Graphics/simpleGLES_screen  
### 5_Simulations/nbody_opengles  
### 5_Simulations/fluidsGLES  
### 5_Simulations/nbody_screen  
###  
RUN apt install -y libgles2-mesa-dev  
  
  
###  
### You should also search 'UBUNTU_PKG_NAME = "nvidia-367"' and replace it to
'UBUNTU_PKG_NAME = "nvidia"'  
### for all matched files in the NVIDIA_CUDA-8.0_Samples folder to make it
works.  
###  
RUN mkdir /usr/lib/nvidia && \  
`### solve for /usr/bin/ld: cannot find -lnvcuvid` \  
`### 3_Imaging/cudaDecodeGL` \  
ln -s /usr/local/nvidia/lib64/libnvcuvid.so.1 /usr/lib/nvidia/libnvcuvid.so &&
\  
`### solve for >>> WARNING - libEGL.so not found, please install libEGL.so
<<<` \  
`### 3_Imaging/EGLStreams_CUDA_Interop `\  
ln -s /usr/local/nvidia/lib64/libEGL.so.1 /usr/lib/nvidia/libEGL.so && \  
`### solve for >>> WARNING - libGLES.so not found, please install libGLES.so
<<<` \  
`### 2_Graphics/simpleGLES_EGLOutput` \  
`### 2_Graphics/simpleGLES` \  
`### 2_Graphics/simpleGLES_screen` \  
`### 5_Simulations/nbody_opengles` \  
`### 5_Simulations/fluidsGLES` \  
`### 5_Simulations/nbody_screen` \  
ln -s /usr/local/nvidia/lib64/libGLESv2_nvidia.so.2
/usr/lib/nvidia/libGLESv2.so  
  
  
##############  
# upgrade  
##############  
RUN apt upgrade -y  
  
##############  
# cleanup  
##############  
# debian - clear apt-get list - Unix & Linux Stack Exchange  
# https://unix.stackexchange.com/questions/217369/clear-apt-get-list  
#  
# bash - autoremove option doesn't work with apt alias - Ask Ubuntu  
# https://askubuntu.com/questions/573624/autoremove-option-doesnt-work-with-
apt-alias  
#  
RUN apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
  
CMD ["bash"]  
  
  

