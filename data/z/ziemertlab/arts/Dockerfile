FROM debian:8  
RUN echo "Installing required libs..."; apt-get update && apt-get install -y
wget python python-dev python-pip liblzma-dev libxml2-dev libxslt-dev
zlib1g-dev libxext-dev libjpeg-dev libfreetype6-dev default-jre-headless mafft
&& \  
wget https://bitbucket.org/ziemertlab/arts/raw/HEAD/requirements.txt && pip
install -r requirements.txt  
RUN echo "Installing antiSMASH..."; wget
"https://bitbucket.org/antismash/antismash/downloads/antismash-3.0.5.tar.gz"
\--no-check-certificate && \  
tar -xf antismash-3.0.5.tar.gz && mv antismash-3.0.5 antismash && rm
antismash-3.0.5.tar.gz  
ADD . /arts  
WORKDIR /arts/  
RUN echo "Adding required binaries"; tar -xzf linux64_bins.tar.gz -C
/usr/local/bin/ && hash -r && mkdir -p results upload run && \  
rm webapp/config/artsapp_default.conf && mv webapp/config/artsapp_docker.conf
webapp/config/artsapp_default.conf && \  
pip install -r requirements.txt && pip install -r /antismash/requirements.txt  
WORKDIR /antismash/antismash/specific_modules/nrpspks  
RUN hmmpress abmotifs.hmm && hmmpress dockingdomains.hmm && hmmpress
ksdomains.hmm && hmmpress nrpspksdomains.hmm && hmmpress
../../generic_modules/smcogs/smcogs.hmm  
WORKDIR /arts/  
  
ENTRYPOINT ["python","runjobs.py","run","-pid","/arts/run/runjobs.pid"]  

