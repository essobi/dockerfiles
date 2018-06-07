FROM lnls/epics-deps:base-3.14-debian-9  
  
ENV COMMIT base-3.14  
  
RUN git clone https://github.com/lnls-sirius/epics-dev.git /tmp/epics-dev && \  
cd /tmp/epics-dev && \  
git checkout ${COMMIT} && \  
./run-all.sh -o -i -c -e yes && \  
cd / && \  
rm -rf /tmp/epics-dev && \  
rm -rf /var/lib/apt/lists/*  

