FROM cwpearson/opencl2.0-intel-cpu  
  
RUN apt-get update && apt-get install --no-install-recommends -y libopencv-
core-dev libopencv-highgui-dev libopencv-imgproc-dev g++ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set the environment variables Chai expects  
ENV CHAI_OCL_INC $OCL_INC  
ENV CHAI_OCL_LIB $OCL_LIB  
  
# Make the Chai OpenCL source files visible to the container  
ADD ./OpenCL1.2 chai/OpenCL1.2  
ADD ./OpenCL2.0 chai/OpenCL2.0  
ADD bin chai/bin  
ENV PATH /chai/bin:$PATH  
WORKDIR chai/OpenCL2.0  
  
# Build OpenCL 2.0 version of all benchmarks  
RUN set -e; \  
for bench in *; do \  
echo $bench; \  
cd $bench; \  
make -j; \  
cd ..; \  
done  

