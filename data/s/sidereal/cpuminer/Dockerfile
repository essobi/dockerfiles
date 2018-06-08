FROM buildpack-deps:stretch  
  
RUN set -x \  
&& cd /root \  
&& git clone https://github.com/macchky/cpuminer.git \  
&& cd cpuminer \  
&& ./autogen.sh \  
&& ./configure CFLAGS="-O3" \  
&& make \  
&& ./minerd --help \  
&& ./minerd --version  
  
FROM buildpack-deps:stretch-curl  
  
COPY \--from=0 /root/cpuminer/minerd /usr/local/bin/  
  
WORKDIR /root  
  
ENTRYPOINT [ "/usr/local/bin/minerd" ]  
  

