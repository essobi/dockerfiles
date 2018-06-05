FROM hasable/arma3-mods:latest  
LABEL maintainer='hasable'  
  
USER root  
# Provides commands & entrypoint  
COPY bin /usr/local/bin  
RUN chmod +x /usr/local/bin/* && sync  
  
# Server user  
ARG USER_NAME=steamu  
USER ${USER_NAME}  
WORKDIR /tmp  
RUN prepare-hc \  
&& install-a3xai-upload \  
&& install-dms \  
&& install-occupation \  
&& install-vemfr \  
&& install-zcp  
  
WORKDIR /opt/arma3  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint", "/opt/arma3/arma3server"]  
CMD ["\"-config=conf/exile.cfg\"", \  
"\"-servermod=@ExileServer;@A3XAI;@AdminToolkitServer;@AdvancedRappelling;@AdvancedUrbanRappelling;@DMS;@Enigma;@ExAd;@Occupation;@VEMF;@ZCP\"",
\  
"\"-mod=@Exile;@EBM;@CBA_A3;@CUPWeapons;@CUPUnits;@CUPVehicles;@R3FArmes;@R3FUnites\"",
\  
"-world=empty", \  
"-autoinit"]  
  

