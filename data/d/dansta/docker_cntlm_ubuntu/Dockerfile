FROM ubuntu:latest  
# we base this on ubuntu  
# set env. replace right most column with values specific to your environment  
ENV CNTLM_PROXY_URL <upstreamproxy:upstreamproxyport>  
ENV CNTLM_PROXY_PORT 3128  
ENV CNTLM_DOMAIN set.to.internal.domain.com  
ENV CNTLM_USERNAME username  
ENV CNTLM_PASSLM hashed_string_passlm  
ENV CNTLM_PASSNTLMv2 hashed_string_passntlmvv2  
  
LABEL maintainer=dansta  
  
# change to some webserver that you know is stable. mine isnt which is why per
default this is commented out  
#HEALTHCHECK --interval=15m --timeout=3s CMD curl -x 127.0.0.1:3128 -f
http://www.kvantmekanik.se || exit 1  
# update and install packages  
RUN apt-get update  
RUN apt-get install -y cntlm  
RUN apt-get install -y rsyslog  
ADD files/etc/cntlm.conf /etc/cntlm.conf  
  
# truncate the file and add the rest of the params  
RUN echo "Username ${CNTLM_USERNAME}" > /etc/cntlm.conf  
RUN echo "Domain ${CNTLM_DOMAIN}" >> /etc/cntlm.conf  
RUN echo "PassLM ${CNTLM_PASSLM}" >> /etc/cntlm.conf  
RUN echo "PassNT ${CNTLM_PASSNT}" >> /etc/cntlm.conf  
RUN echo "PassNTLMv2 ${CNTLM_PASSNTLMv2}" >> /etc/cntlm.conf  
RUN echo "Proxy ${CNTLM_PROXY_URL}" >> /etc/cntlm.conf  
RUN echo "Listen ${CNTLM_PROXY_PORT}" >> /etc/cntlm.conf  
RUN echo "NoProxy *.${CNTLM_DOMAIN}" >> /etc/cntlm.conf  
# bug workaround or cntlm will crash. it needs the last empty row  
RUN echo "" >> /etc/cntlm.conf  
  
# document port usage for docker in case you are going to use it as a service  
EXPOSE ${CNTLM_PROXY_PORT}/tcp  
  
# logging for debug. logging should be handled by your support team  
RUN service rsyslog start  
  
# import pki for security proxy, don't forget to copy them to
files/certificates or this step will fail  
# ADD files/certificates/* /usr/local/share/ca-certificates/  
# test cntlm for build, run in foreground  
CMD /usr/sbin/cntlm -f -g  
  

