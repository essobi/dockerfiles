FROM pwlb/julia-bio  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libxt6 libgl1-mesa-glx libxrender1 && \  
rm -rf /var/lib/apt/lists/*  
  
COPY install /install  
RUN julia -e 'include("/install/install.jl")'  
  
COPY src /pipeline  
  
ENTRYPOINT ["julia","/pipeline/julia/demultiplex.jl","-c"]  
CMD ["/config/demultiplexer.yml"]  

