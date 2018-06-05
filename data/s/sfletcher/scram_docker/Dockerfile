FROM continuumio/miniconda3  
  
  
WORKDIR /software  
RUN wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz  
  
ENV PATH "$PATH:/usr/local/go/bin"  
RUN conda config --add channels bioconda  
RUN conda install --yes \  
'bokeh' \  
'matplotlib' \  
'numpy' \  
'jupyter' \  
'pandas' \  
'fastx_toolkit' \  
'perl-list-moreutils' \  
'blast' \  
'fastqc'  
RUN sed -i "s/^#\\!.*$/#\\!\/usr\/bin\/env perl/"
/opt/conda/bin/update_blastdb.pl  
  
RUN apt-get update &&\  
apt-get install -y \  
nano \  
htop \  
tree \  
curl  
  
  
RUN go get github.com/sfletc/scram github.com/sfletc/scramPkg
github.com/spf13/cobra github.com/spf13/viper github.com/montanaflynn/stats  
RUN cd /root/go/src/github.com/sfletc/scram && \  
go install  
  
WORKDIR /scram  
RUN git clone https://github.com/sfletc/scram_plot.git  
  
WORKDIR /scram_plot  
RUN cd /scram_plot && \  
cp /scram/scram_plot/scram_plot/* ./  
  
ENV PATH "$PATH:/root/go/bin"  
WORKDIR /work  
  
CMD jupyter notebook --port=8888 --no-browser --ip='*' \--allow-root  

