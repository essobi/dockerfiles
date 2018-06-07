FROM ubuntu:16.10  
MAINTAINER Johannes Doerfert <doerfert@cs.uni-saarland.de>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential cmake \  
git git-svn kpartx libglib2.0-dev groff tclsh \  
subversion zlib1g-dev flex libfdt1 git libfdt-dev libpixman-1-0 \  
libpixman-1-dev python-virtualenv sed python-dev vim emacs byacc flex  
  
RUN git clone https://github.com/jdoerfert/CGO17_ArtifactEvaluation.git /ae  
  
CMD git -C /ae fetch && git -C /ae reset --hard origin/master  
CMD bash -c "python /ae/scripts/artifact_eval.py; bash"  

