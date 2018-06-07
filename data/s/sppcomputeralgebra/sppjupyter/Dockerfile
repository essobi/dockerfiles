## Dockerfile for the DFG SPP Computeralgebra Software Jupyter kernels  
FROM sppcomputeralgebra/sppdocker  
  
MAINTAINER Sebastian Gutsche <sebastian.gutsche@gmail.com>  
  
ADD install_scripts /tmp/jupyter_install_scripts  
RUN sudo chown -R spp:spp /tmp/jupyter_install_scripts \  
&& chmod +x /tmp/jupyter_install_scripts/install_*.sh  
WORKDIR /tmp/jupyter_install_scripts  
  
## Install jupyter  
RUN ./install_jupyter.sh  
  
## Install kernels  
RUN ./install_kernels.sh  
  
EXPOSE 8888  
WORKDIR /home/spp  
  
CMD /bin/bash -c "sudo jupyter notebook --no-browser"

