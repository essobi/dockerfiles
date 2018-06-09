#  
# ReinforcementLearning.jl Dockerfile  
#  
# https://github.com/benhamner/ReinforcementLearning.jl/tree/master/Dockerfile  
#  
# docker build -t="benhamner/reinforcement_learning.jl" .  
# docker run -it benhamner/reinforcement_learning.jl /bin/bash  
# Pull base image.  
FROM ubuntu:14.04  
# Install Julia and clone ReinforcementLearning.jl  
RUN cd /  
RUN apt-get install git software-properties-common curl wget gettext libcairo2
libpango1.0-0 -y  
RUN add-apt-repository ppa:staticfloat/julia-deps -y  
RUN add-apt-repository ppa:staticfloat/julianightlies -y  
RUN apt-get update -qq -y  
RUN apt-get install libpcre3-dev julia -y  
RUN julia -e 'Pkg.init()'  
RUN julia -e 'Pkg.clone("https://github.com/dcjones/Showoff.jl");
Pkg.clone("https://github.com/benhamner/ReinforcementLearning.jl");
Pkg.checkout("Gadfly"); Pkg.checkout("MachineLearning");
Pkg.checkout("ReinforcementLearning"); Pkg.pin("ReinforcementLearning");
Pkg.resolve();'  
RUN julia -e 'using ReinforcementLearning; @assert
isdefined(:ReinforcementLearning); @assert typeof(ReinforcementLearning) ===
Module'  
  
CMD ["julia", "/root/.julia/v0.4/ReinforcementLearning/test/runtests.jl"]  

