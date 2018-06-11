FROM ubuntu:17.10  
COPY \  
cli.py.patch \  
.yamllint \  
/  
  
RUN apt-get update \  
&& RUNTIME_DEPS=' \  
python3-pkg-resources \  
yamllint \  
' \  
BUILD_DEPS=' \  
patch \  
' \  
&& apt-get install -y --no-install-recommends ${RUNTIME_DEPS} ${BUILD_DEPS} \  
# patch UnicodeDecodeError  
&& patch -p0 < /cli.py.patch \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& apt-get install -y --no-install-recommends ${RUNTIME_DEPS} \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["yamllint"]  
CMD ["--help"]  

