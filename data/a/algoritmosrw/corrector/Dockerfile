# -*- docker-image-name: "algoritmosrw/corrector" -*-  
FROM ubuntu:artful  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y gcc g++ clang libgtest-dev make valgrind time python3
python3-jinja2 && \  
make -f /usr/src/googletest/googletest/make/Makefile -C /usr/local/lib \  
gtest.a && ln -s gtest.a /usr/local/lib/libgtest.a  
  
COPY ["*.py", "*.j2", "/"]  
  
USER nobody  
WORKDIR /tmp  
  
ENTRYPOINT ["/worker.py"]  
  
# vi:et  

