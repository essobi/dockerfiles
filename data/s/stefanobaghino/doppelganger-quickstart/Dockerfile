FROM continuumio/anaconda  
  
RUN apt-get update && apt-get install -y gcc g++ unzip  
  
RUN mkdir -p /opt/sidewalklabs && cd /opt/sidewalklabs && git clone
https://github.com/sidewalklabs/doppelganger.git && cd doppelganger && pip
install .  
  
RUN cd /opt/sidewalklabs/doppelganger/examples/sample_data && unzip
2010_puma_tract_mapping.txt.zip  
  
COPY fix_doppelganger_example_full.py /opt/sidewalklabs/doppelganger  
  
RUN /opt/sidewalklabs/doppelganger/fix_doppelganger_example_full.py  
  
EXPOSE 8888  
CMD /opt/conda/bin/jupyter notebook --notebook-
dir=/opt/sidewalklabs/doppelganger/examples --ip='*' \--port=8888 --no-browser  

