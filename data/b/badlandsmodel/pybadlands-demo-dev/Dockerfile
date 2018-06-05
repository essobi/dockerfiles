# Pull base image.  
FROM badlandsmodel/pybadlands-dependencies  
  
MAINTAINER Ian Howson  
  
WORKDIR /build  
RUN git clone https://github.com/badlands-model/pyBadlands.git  
WORKDIR /build/pyBadlands/pyBadlands/libUtils  
RUN make  
RUN pip install -e /build/pyBadlands  
  
WORKDIR /build  
RUN git clone https://github.com/badlands-model/pyBadlands-Companion.git  
RUN pip install -e /build/pyBadlands-Companion  
  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
# Copy cluster configuration  
RUN mkdir /root/.ipython  
COPY profile_mpi /root/.ipython/profile_mpi  
  
RUN mkdir /workspace && \  
mkdir /workspace/volume && \  
mkdir /workspace/companion  
  
# Copy test files to workspace  
RUN cp -av /build/pyBadlands/Examples/* /workspace/  
RUN cp -av /build/pyBadlands-Companion/notebooks/* /workspace/companion/  
  
COPY run.sh /build  
RUN chmod +x /build/run.sh  
  
# setup space for working in  
VOLUME /workspace/volume  
  
# launch notebook  
WORKDIR /workspace  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
ENV
LD_LIBRARY_PATH=/workspace/volume/pyBadlands/pyBadlands/libUtils:/build/pyBadlands/pyBadlands/libUtils  
CMD /build/run.sh  
  

