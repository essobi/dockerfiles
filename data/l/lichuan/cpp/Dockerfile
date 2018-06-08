FROM lichuan/ubuntu  
RUN apt-get install -y \  
clang \  
cscope \  
g++ \  
gdb \  
make \  
ruby \  
scons \  
yasnippet  
RUN mkdir -p /root/download/auto-complete  
RUN mkdir -p /root/.emacs.d/auto-complete  
RUN mkdir -p /root/.emacs.d/other  
RUN mkdir -p /root/.emacs.d/color-theme-6.6.0  
RUN mkdir -p /root/.emacs.d/cscope  
COPY auto-complete /root/download/auto-complete/  
COPY other /root/.emacs.d/other/  
COPY color-theme-6.6.0 /root/.emacs.d/color-theme-6.6.0/  
COPY cscope /root/.emacs.d/cscope/  
COPY .emacs /root/.emacs  
COPY lccscope /root/bin/  
RUN cd /root/download/auto-complete && make install DIR=/root/.emacs.d/auto-
complete  
RUN chmod 755 /root/bin/lccscope  
RUN rm -rf /root/download/auto-complete  

