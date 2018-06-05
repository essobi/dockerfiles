FROM wqael/anaconda:5.1-py3.6-ubuntu17.10  
LABEL description="Prebuilt jupyter environment on Ubuntu."  
LABEL maintainer="https://github.com/rlan/anaconda"  
  
# Add Tini  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Run under Tini  
WORKDIR /root  
CMD ["jupyter", "notebook", "--ip=*", "--port=8888", "--allow-root", "--no-
browser"]  

