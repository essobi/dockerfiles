FROM andrewnk/turtlecoin-base  
  
ARG RPC_BIND_PORT=11898  
ENV RPC_BIND_PORT=${RPC_BIND_PORT}  
  
ARG
CHECKPOINTS_FILE_LOCATION=https://github.com/turtlecoin/checkpoints/raw/master/  
ENV CHECKPOINTS_FILE_LOCATION=${CHECKPOINTS_FILE_LOCATION}  
  
ARG CHECKPOINTS_FILE=checkpoints.csv  
ENV CHECKPOINTS_FILE=${CHECKPOINTS_FILE}  
  
ARG TURTLECOIN_DIR=/home/turtlecoin/.TurtleCoin  
ENV TURTLECOIN_DIR=${TURTLECOIN_DIR}  
RUN apt-get update && \  
apt-get install -y \  
wget  
  
RUN mkdir ${TURTLECOIN_DIR}  
  
WORKDIR ${TURTLECOIN_DIR}  
  
COPY turtlecoind.conf ${TURTLECOIN_DIR}  
RUN wget ${CHECKPOINTS_FILE_LOCATION}${CHECKPOINTS_FILE}  
RUN chown -R turtlecoin:turtlecoin ${TURTLECOIN_DIR}  
RUN apt-get remove -y wget && \  
apt-get autoremove -y  
  
EXPOSE ${RPC_BIND_PORT}  
  
CMD su - turtlecoin -c "TurtleCoind --config-file
${TURTLECOIN_DIR}/turtlecoind.conf --load-checkpoints
${TURTLECOIN_DIR}/${CHECKPOINTS_FILE}"  

