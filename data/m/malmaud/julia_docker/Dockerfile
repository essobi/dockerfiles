FROM julia:0.4  
MAINTAINER Jon Malmaud (malmaud@gmail.com)  
VOLUME /data  
CMD julia  
  
RUN apt-get update && \  
apt-get install -y sudo gcc g++ && \  
rm -rf /var/lib/apt/lists/*  
RUN julia -e 'Pkg.clone("https://github.com/IntelLabs/CompilerTools.jl.git")'
# Install the CompilerTools package on which this package depends.  
RUN julia -e
'Pkg.clone("https://github.com/IntelLabs/ParallelAccelerator.jl.git")' #
Install this package.  
RUN julia -e 'Pkg.build("ParallelAccelerator")' # Build the C++ runtime
component of the package.  

