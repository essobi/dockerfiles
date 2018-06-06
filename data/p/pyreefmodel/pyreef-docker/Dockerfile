# Pull base image.  
FROM pyreefmodel/pyreef-dependencies-docker  
  
MAINTAINER Tristan Salles  
  
WORKDIR /build  
RUN pip install -e git+https://github.com/hplgit/odespy.git#egg=odespy  
WORKDIR /build/src/odespy  
RUN python setup.py install  
  
#WORKDIR /build  
#RUN git clone https://github.com/pyReef-model/pyReef.git  
#WORKDIR /build/pyReef/pyReef/libUtils  
#RUN make clobber  
#RUN make dist  
#RUN pip install -e /build/pyReef  
WORKDIR /build  
RUN git clone https://github.com/pyReef-model/pyReefCore.git  
RUN pip install -e /build/pyReefCore  
  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
# Copy cluster configuration  
RUN mkdir /root/.ipython  
COPY profile_mpi /root/.ipython/profile_mpi  
  
RUN mkdir /workspace && \  
mkdir /workspace/volume  
  
# Copy test files to workspace  
RUN cp -av /build/pyReefCore/Tests /workspace/  
  
COPY run.sh /build  
RUN chmod +x /build/run.sh  
  
# setup space for working in  
VOLUME /workspace/volume  
  
# launch notebook  
WORKDIR /workspace  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
ENV
LD_LIBRARY_PATH=/workspace/volume/pyReefCore/pyReefCore/libUtils:/build/pyReefCore/pyReefCore/libUtils  
CMD /build/run.sh  

