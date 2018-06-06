FROM perfectweb/base:v3  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
USER root  
WORKDIR /  
  
RUN apt-get install -qqy libmicrohttpd-dev ocl-icd-opencl-dev  
  
RUN git clone https://github.com/fireice-uk/xmr-stak-amd.git  
RUN cd /xmr-stak-amd && cmake . && make  
  
ENV WALLET
4GdoN7NCTi8a5gZug7PrwZNKjvHFmKeV11L6pNJPgj5QNEHsN6eeX3DaAQFwZ1ufD4LYCZKArktt113W7QjWvQ7CWGGFVGSSXdKSPo6pG3  
ENV PASSWORD x  
ENV POOLHOSTNAME pool.minexmr.com  
ENV PORT 7777  
ENV RAWINTENSITY 1000  
ENV WORKSIZE 8  
COPY config.tpl /xmr-stak-amd/  
COPY entrypoint.sh /xmr-stak-amd/  
RUN chmod +x /xmr-stak-amd/entrypoint.sh  
  
WORKDIR /xmr-stak-amd  
  
ENTRYPOINT ["/xmr-stak-amd/entrypoint.sh"]  

