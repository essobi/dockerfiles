FROM ontouchstart/julia-master  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
ADD pkg.jl /pkg.jl  
ADD fibo.jl /fibo.jl  
RUN /julia/julia pkg.jl  
ENTRYPOINT ["/julia/julia", "fibo.jl"]  
EXPOSE 8888  

