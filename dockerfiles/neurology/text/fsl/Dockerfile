FROM neurodebian:jessie
MAINTAINER Jan-Gerd Tenberge <jan-gerd.tenberge@uni-muenster.de>

ADD sources.list /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
RUN apt-get update
RUN apt-get install --no-install-recommends -y fsl-complete=5.0.7-1~nd80+1
RUN echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc
