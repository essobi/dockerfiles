FROM ubuntu:latest  
  
# Copy useful "minimal" commands from util  
COPY util/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ENV PATH /opt/conda/bin:$PATH  
  
RUN min-apt bzip2 ca-certificates curl git wget  
  
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
echo ". /opt/conda/etc/profile.d/conda.sh" >> /etc/bash.bashrc && \  
echo "conda activate base" >> ~/.bashrc && \  
conda update --all -q && \  
min-conda conda-build  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  
  
RUN conda create -qyn psi python=3.6.* bokeh numba numpy pandas plotly seaborn
&& \  
clean-conda  
  
RUN chmod +x /opt/conda/etc/profile.d/conda.sh

