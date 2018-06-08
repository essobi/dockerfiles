FROM andreadotti/geant4-base:latest  
  
MAINTAINER Andrea Dotti (adotti@slac.stanford.edu)  
  
RUN apt update -y && apt install -y libssl-dev libffi-dev \  
python3-dev build-essential git jq \  
python3-pip sudo vim virtualenv  
  
RUN pip3 install --upgrade pip && pip3 install --prefix /usr/local \--upgrade
blobxfer  
RUN pip3 install --prefix /usr/local azure-cli  
RUN ln -s /usr/bin/python3 /usr/bin/python  
  
# Batch shipuard requires sudo for installation  
# and cannot be installed as root  
RUN useradd -ms /bin/bash g4-azure  
RUN echo "g4-azure ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
USER g4-azure  
WORKDIR /home/g4-azure  
  
RUN git clone https://github.com/Azure/batch-shipyard.git  
RUN cd batch-shipyard && ./install.sh -3 -e shipyard.venv  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
COPY az-batch config.json credentials-template.json jobs-example.json
pool.json summary.json *.sh *.md /geant4-val-azure/  
  
ENV PATH="$PATH:/geant4-val-azure:/home/g4-azure/batch-shipyard"  

