FROM rootproject/root-ubuntu16  
USER root  
WORKDIR /tmp/  
RUN git clone \--recurse-submodules https://github.com/tylern4/hipo2root.git \  
&& cd hipo2root \  
&& ./make_hipo2root.py --json bankdefs/rec_particle.json \  
&& make -j$(nproc) \  
&& mv hipo2root /usr/bin/ \  
&& rm -rf /tmp/*  
  
ENTRYPOINT ["/usr/bin/hipo2root"]  

