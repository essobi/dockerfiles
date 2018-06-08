# run with -q (workaround for https://github.com/dotcloud/docker/issues/3172)  
# like this:  
# sudo docker build -q -t julia1102 .  
  
FROM ubuntu  
RUN apt-get install -y make gcc g++ gfortran git perl wget curl m4 patch bzip2
libncurses5-dev && apt-get clean  
RUN git clone git://github.com/JuliaLang/julia.git /tmp/julia && cd /tmp/julia
&& make -j8 && cp -r usr/* /usr && rm -rf /tmp/julia && ln -s /usr/bin/julia-
readline /usr/bin/julia && ln -s /bin/bash /usr/bin/sudo  

