# Linux dev environment for LEDE project  
  
FROM jlcs/omega2-docker-built-half  
  
RUN make toolchain/install  
  
ENV PATH "$PATH:/lede/staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/bin"  
ENV STAGING_DIR "/lede/staging_dir"  
ENV CFLAGS=-I/lede/staging_dir/target-mipsel_24kc_musl/usr/include  
ENV LDFLAGS=-L/lede/staging_dir/target-mipsel_24kc_musl/usr/lib  
# Use this command to run with shared directory:  
# docker run -it --name omega2-sdk-app -v /my_host_dir:/remote
jlcs/omega2-sdk-built bash  

