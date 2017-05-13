FROM jupyter/base-notebook:latest

RUN conda install --yes --no-pin \
  geopandas \
  scikit-learn \
  statsmodels \
  seaborn

# enable importing jupyter notebooks as modules
RUN pip install jupynbimp
