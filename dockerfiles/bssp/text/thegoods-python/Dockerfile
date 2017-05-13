# BSSP Base Python Docker Image
FROM python:3.6.0
ENV TERM screen-256color
# Apt-get Deps:
RUN apt-get update && apt-get upgrade -y \
	&& apt-get install build-essential gcc g++ gfortran liblapack-dev python3-dev python3-opengl -y \
	&& apt-get install less vim rsync libhdf5-dev libsuitesparse-dev libfreetype6-dev pkg-config -y \
	&& apt-get install libmariadb2 mariadb-client-10.0 -y
# Python deps:
RUN pip install -U pip && pip install -U pip cython && pip install -U numpy  \
	&& pip install -U oauth2 awscli bokeh bottleneck bs4 cachetools cairocffi folium geopy h5py \
	&& pip install -U hdfs ipdb ipython jellyfish line_profiler lxml matplotlib memory_profiler mpld3 mpmath \
	&& pip install -U mysqlclient nltk numexpr numexpr pandas pandas_datareader paramiko patsy pillow plotly \
	&& pip install -U pycountry pydrill pymc3 python-dateutil pytz qgrid requests schedule scikit-learn scipy \
	&& pip install -U seaborn six sqlalchemy statsmodels sympy tables tabulate us wordcloud xlrd zipcode
