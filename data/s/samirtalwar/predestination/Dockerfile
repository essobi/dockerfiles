FROM continuumio/miniconda3  
  
RUN set -ex; \  
apt-get update -qq; \  
apt-get install -qqy zsh  
  
WORKDIR /app  
  
ENV PATH /opt/conda/envs/app/bin:$PATH  
COPY environment.yml ./  
RUN set -ex; \  
conda env create --name=app; \  
rm -r /opt/conda/pkgs  
  
COPY . ./  
  
CMD ["./web"]  

