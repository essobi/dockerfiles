FROM tsutomu7/python-opencv  
  
RUN conda install -y pillow flask networkx && \  
pip install four_color && \  
conda update -y --all && \  
find /opt -name __pycache__ | xargs rm -r && \  
sudo rm -rf $HOME/.c* /opt/conda/pkgs/* \  
/opt/conda/lib/python3.5/site-packages/pulp/solverdir/cbc/[ow]* \  
/opt/conda/lib/python3.5/site-packages/pulp/solverdir/cbc/linux/32  
COPY sample.py sample.png $HOME/  
CMD ["sh", "-c", "python -m four_color"]  

