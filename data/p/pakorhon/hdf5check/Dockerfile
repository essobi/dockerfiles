FROM ubuntu:16.04  
# Install dextractor  
RUN apt-get update && apt-get install -y git python build-essential parallel
libhdf5-dev  
WORKDIR /root  
RUN git clone -b 'V1.0' \--single-branch --depth 1
https://github.com/thegenemyers/DEXTRACTOR  
WORKDIR DEXTRACTOR  
RUN mv Makefile Makefile.orig && sed 1,1d Makefile.orig | sed
's/\/usr\/local\/hdf5/\/usr\/lib\/x86_64-linux-gnu\/hdf5\/serial/1' > Makefile  
RUN make && mv dextract /usr/local/bin  
WORKDIR /root  
RUN rm -rf DEXTRACTOR  
RUN git clone -b 'v1.0.2-beta' \--single-branch --depth 1
https://github.com/vetscience/Tools  
WORKDIR Tools  
RUN chmod uog+x /root && chmod uog+rwx /root/Tools && chmod uog+x
/root/Tools/Assembly && chmod uog+x /root/Tools/Assembly/hdf5Check.py  
ENV PYTHONPATH /root/Tools  
ENTRYPOINT ["/root/Tools/Assembly/hdf5Check.py"]  

