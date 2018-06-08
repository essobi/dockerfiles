FROM alisw/slc6-cvmfs  
ENTRYPOINT zsh -c "cd /usr/bin && \  
curl -LO https://raw.githubusercontent.com/dberzano/alien-
workqueue/master/alien_wq_worker.sh && \  
chmod +x alien_wq_worker.sh && \  
mkdir /root/WQ_{WORKDIR,DRAIN} && \  
./alien_wq_worker.sh workers"  
# Configuration: change the WQ Foremen node (WQ_FOREMEN) and the number of
Foremen running (WQ_NUM_FOREMEN).  
ENV WQ_FOREMEN=aliplancton.cern.ch \  
WQ_NUM_FOREMEN=6 \  
WQ_DEBUG=1  

