FROM hasable/arma3-bots:latest  
LABEL maintainer='hasable'  
  
ARG USER_NAME=steamu  
  
USER root  
COPY bin/docker-entrypoint /usr/local/bin/  
RUN apt-get update \  
&& apt-get install -y rsync \  
&& apt-get clean \  
&& chmod +x /usr/local/bin/docker-entrypoint \  
&& sync  
  
WORKDIR /home/steamu  
COPY sources sources  
RUN chown -R ${USER_NAME}:${USER_NAME} sources  
  
# Server user  
USER ${USER_NAME}  
WORKDIR /opt/arma3  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint", "/opt/arma3/arma3server"]  
CMD ["\"-config=conf/exile.cfg\"", \  
"\"-servermod=@ExileServer;@A3XAI;@AdminToolkitServer;@AdvancedRappelling;@AdvancedUrbanRappelling;@DMS;@Enigma;@ExAd;@Occupation;@VEMF;@ZCP\"",
\  
"\"-mod=@Exile;@EBM;@CBA_A3;@CUPWeapons;@CUPUnits;@CUPVehicles;@R3FArmes;@R3FUnites\"",
\  
"-world=empty", \  
"-autoinit"]  

