FROM julia:0.6.2  
RUN apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends hdf5-tools build-essential
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN julia -e 'map(Pkg.add, ["Sobol", "MAT", "PlotlyJS", "QuantEcon",
"BasisMatrices"])'  
  
RUN julia -e 'using Sobol, MAT, PlotlyJS, QuantEcon, BasisMatrices'  
  
CMD ["/usr/local/julia/bin/julia", "-O3",
"/var/programfiles/NewKeynesian/julia/main.jl", "table"]  

