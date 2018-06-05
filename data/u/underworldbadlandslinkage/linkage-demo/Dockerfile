FROM underworldbadlandslinkage/linkage-models  
  
MAINTAINER Ian Howson  
  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
# Copy cluster configuration  
RUN mkdir /root/.ipython  
COPY profile_mpi /root/.ipython/profile_mpi  
  
# setup space for working in  
RUN mkdir /workspace && \  
mkdir /workspace/volume  
  
# Install demo notebooks  
WORKDIR /build  
RUN cp -av /build/BasinGenesisHub/linkage/examples/* /workspace/  
  
VOLUME /workspace/volume  
  
COPY run.sh /build  
RUN chmod +x /build/run.sh  
  
# script for xvfb-run. all docker commands will effectively run under this via
the entrypoint  
RUN printf "#\041/bin/sh \n rm -f /tmp/.X99-lock && xvfb-run -s '-screen 0
1600x1200x16' \$@" >> /usr/local/bin/xvfbrun.sh && \  
chmod +x /usr/local/bin/xvfbrun.sh  
  
# launch notebook  
WORKDIR /workspace  
# expose notebook port  
EXPOSE 8888  
# expose glucifer port  
EXPOSE 9999  
# note we also use xvfb which is required for viz  
ENTRYPOINT ["/usr/local/bin/tini", "--", "xvfbrun.sh"]  
  
ENV PYTHONPATH=/build/underworld2  
ENV LD_LIBRARY_PATH=/build/pyBadlands/pyBadlands/libUtils  
CMD /build/run.sh  
  

