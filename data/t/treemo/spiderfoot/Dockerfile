FROM python:2  
# Add non privileged user  
RUN useradd -m user  
  
# install app  
WORKDIR /tmp  
RUN curl -L https://api.github.com/repos/smicallef/spiderfoot/tarball | tar xz  
RUN mv *spiderfoot* /usr/src/app  
WORKDIR /usr/src/app  
RUN chown user -R /usr/src/app  
  
# install dependancies  
RUN apt-get update  
RUN apt-get install -y swig  
RUN pip install -r requirements.txt  
  
# clean / optimise docker size  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/* /var/tmp/*  
  
# check install  
RUN python -c 'import sf'  
  
# running  
USER user  
ENV BINDING_ADDRESS ${BINDING_ADDRESS:-0.0.0.0:8080}  
ENTRYPOINT python sf.py $BINDING_ADDRESS  
  

