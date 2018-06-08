# Pandas with SciPy & Jupyter notebook  
#  
# docker run --rm -it pottava/pandas:0.19 ipython  
# docker run --rm -it -p 80:8888 pottava/pandas:0.19  
  
FROM pottava/scipy:0.19-note  
  
ENV NUMPY_VERSION=1.12.1 \  
MATPLOTLIB_VERSION=2.0.0 \  
PANDAS_VERSION=0.19.2  
  
RUN apk --no-cache add freetype \  
&& apk --no-cache add --virtual build-deps g++ python3-dev \  
lapack-dev g++ gfortran freetype-dev \  
&& ln -s /usr/bin/python3 /usr/bin/python \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
# Install NumPy again for some libraries  
&& pip3 install "numpy == ${NUMPY_VERSION}" \  
# Install Matplotlib for 2D plotting  
&& pip3 install "matplotlib == ${MATPLOTLIB_VERSION}" \  
# Install Pandas  
&& pip3 install "pandas == ${PANDAS_VERSION}" \  
# Clean up  
&& find / -type d -name tests -depth -exec rm -rf {} \; \  
&& find / -type d -name test -depth -exec rm -rf {} \; \  
&& find / -type d -name \\__pycache__ -depth -exec rm -rf {} \; \  
&& find / -type d -name '*.egg-info' -depth -exec rm -rf {} \; \  
&& apk del --purge -r build-deps \  
&& rm -rf /root/.cache  

