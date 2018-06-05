FROM python:3.4  
# Run as non-root, eventually  
RUN groupadd -r slamon && useradd -r -g slamon slamon  
  
# Install SLAMon Python Agent  
ADD . /workspace  
WORKDIR /workspace  
RUN pip install .  
RUN rm -rf /workspace  
  
# Change to a non-root user  
USER slamon  
  
CMD ["sh", "-c", "slamon-agent -u ${AFM} -l ${HANDLERS} ${EXTRA_FLAGS}"]  

