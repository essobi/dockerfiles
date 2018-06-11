# Alpine Linux miniconda with Jupyter  
# youske/alpine-conda based  
FROM youske/alpine-conda:miniconda  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.geeplus.description="alpine jupyter image" \  
com.geeplus.role="jupyter baseimage"  
  
ENV LANG=C.UTF-8  
  
COPY ipython_config.py.tmpl /tmp/ipython_config.py  
RUN BUILD='alpine-sdk linux-headers nodejs gcc g++ gfortran make cmake python-
dev freetype-dev musl-dev python-dev libpng-dev libxml2-dev libxslt-dev' && \  
apk update --no-cache && apk add --no-cache --virtual=build-deps ${BUILD} && \  
PACKAGE='jupyter jupyter_contrib_nbextensions
jupyter_nbextensions_configurator jupyter_dashboards jupyter_sphinx_theme
ipyparallel ipywidgets jupyter_cms tqdm pandas pandas-datareader pandas-td
scipy numpy matplotlib bokeh cython pymysql sqlalchemy jupyter_kernel_gateway
bash_kernel metakernel metakernel_bash metakernel_python paramiko folium lxml
nltk' && \  
pip install ${PACKAGE} && \  
jupyter contrib nbextension install --sys-prefix && \  
jupyter nbextension enable --py widgetsnbextension --sys-prefix && \  
jupyter nbextensions_configurator enable --sys-prefix && \  
jupyter dashboards quick-setup --sys-prefix && \  
jupyter cms quick-setup --sys-prefix && \  
ipcluster nbextension enable && \  
python -m bash_kernel.install && \  
# kernels  
# user settings  
mkdir -p /home/admin/.jupyter && mkdir -p /home/admin/.ipython/profile_default
&& \  
cp /tmp/ipython_config.py
/home/admin/.ipython/profile_default/ipython_config.py && \  
chown -R admin:admin /home/admin && \  
# remove cache  
rm -rf /tmp/* /var/cache/apk/* && rm -rf /root/.cache  
  
  
EXPOSE 8888  
CMD ["gosu","admin","jupyter","notebook","--no-browser", "--ip=*","--
port=8888","--notebook-dir=/workdir"]  

