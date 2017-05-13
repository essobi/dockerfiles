### RNEURO with FSL and AFNI
FROM muschellij2/rneuro_fsl
# RUN wget -O- http://neuro.debian.net/lists/sid.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list \
# && apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
RUN apt-get update \
    && apt-get install -y afni

CMD ["bash"]

