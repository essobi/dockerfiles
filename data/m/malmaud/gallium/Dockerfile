FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y bar time binutils gcc g++ libssl-dev gfortran curl git
xz-utils python m4 make cmake bzip2  
RUN git clone https://github.com/JuliaLang/julia.git /julia  
WORKDIR /julia  
ADD Make.user .  
RUN make  
ADD julia_init.jl /root  
RUN /julia/julia /root/julia_init.jl  
ENTRYPOINT ["/julia/julia"]  

