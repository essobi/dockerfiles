FROM debian:stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -yqq --no-install-recommends \  
build-essential \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TARBALL_URL http://bebop.cs.berkeley.edu/smc/tarballs  
  
RUN curl -O http://bebop.cs.berkeley.edu/smc/tarballs/bebop_make.tar.gz  
RUN curl -O http://bebop.cs.berkeley.edu/smc/tarballs/bebop_util.tar.gz  
RUN curl -O
http://bebop.cs.berkeley.edu/smc/tarballs/sparse_matrix_converter.tar.gz  
  
RUN tar xvzf bebop_make.tar.gz  
RUN tar xvzf bebop_util.tar.gz  
RUN tar xvzf sparse_matrix_converter.tar.gz  
  
RUN sed -i 's/USE_PTHREADS=1/USE_PTHREADS=0/g' bebop_make/options  
  
RUN make -C bebop_util  
RUN make -C sparse_matrix_converter  
  
RUN cp bebop_util/libbebop_util.so /usr/local/lib  
RUN cp sparse_matrix_converter/libsparse_matrix_converter.so /usr/local/lib  
  
RUN ldconfig  
  
RUN cp sparse_matrix_converter/sparse_matrix_converter /usr/local/bin  
  
ENTRYPOINT ["sparse_matrix_converter"]  

