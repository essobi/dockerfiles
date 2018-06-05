FROM bids/base_fsl  
  
RUN apt-get update && \  
apt-get install -y git && \  
apt-get install -y python3  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PYTHONPATH=""  
COPY run.py /run.py  
COPY version /version  
# Make the bip directory and put it in the path  
RUN mkdir /usr/local/bip  
ENV BIP_HOME=/usr/local/bip  
ENV PATH=${BIP_HOME}:${PATH}  
  
# git clone with a shallow git tree to reduce bloat  
RUN git clone \--depth 1 https://dpat@bitbucket.org/dpat/bipbids.git
/usr/local/bip  
# remove the shallow .git tree to save space  
RUN rm -rf /usr/local/bip/.git  
  
ENTRYPOINT ["/run.py"]  

