FROM ibmcom/mq:9  
MAINTAINER Shane Genschaw  
  
ENV LICENSE accept  
ENV MQ_QMGR_NAME QM.DEV  
ENV MQ_USER emp-sys  
ENV MQ_PASSWORD secr3T#1  
RUN useradd $MQ_USER -G mqm && \  
echo $MQ_USER:$MQ_PASSWORD | chpasswd && \  
useradd sa_empapi -G mqm && \  
echo "sa_empapi:$MQ_PASSWORD" | chpasswd && \  
useradd sa_empesb -G mqm && \  
echo "sa_empesb:$MQ_PASSWORD" | chpasswd && \  
useradd sa_empmsg -G mqm && \  
echo "sa_empmsg:$MQ_PASSWORD" | chpasswd  
COPY mqm/config.mqsc /etc/mqm/  

