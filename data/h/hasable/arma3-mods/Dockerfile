FROM hasable/arma3-exile:latest  
LABEL maintainer='hasable'  
# Server user  
ARG USER_NAME=steamu  
ARG USER_UID=60000  
  
# Take long time, add it first to reuse cache  
USER root  
COPY resources /tmp  
COPY cache /tmp/cache  
RUN chown -R 60000:60000 /tmp/cache \  
&& chown -R 60000:60000 /tmp/CfgTraders.hpp  
  
USER root  
  
# Provides commands & entrypoint  
COPY bin /usr/local/bin  
RUN chmod +x \  
/usr/local/bin/google-download \  
/usr/local/bin/install-cup-weapons \  
/usr/local/bin/install-cup-units \  
/usr/local/bin/install-cup-vehicles \  
/usr/local/bin/install-r3f-units \  
/usr/local/bin/install-r3f-weapons \  
/usr/local/bin/install-trader-mod  
  
ARG USER_NAME=steamu  
USER ${USER_NAME}  
WORKDIR /tmp  
  
# Install CUP Weapons  
RUN install-cup-weapons \  
&& install-cup-units \  
&& install-cup-vehicles \  
&& install-r3f-units \  
&& install-r3f-weapons \  
&& install-trader-mod  
  
WORKDIR /opt/arma3  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint", "/opt/arma3/arma3server"]  
CMD ["\"-config=conf/exile.cfg\"", \  
"\"-servermod=@ExileServer;@AdminToolkitServer;@AdvancedRappelling;@AdvancedUrbanRappelling;@Enigma;@ExAd\"",
\  
"\"-mod=@Exile;@EBM;@CBA_A3;@CUPWeapons;@CUPUnits;@CUPVehicles;@R3FArmes;@R3FUnites\"",
\  
"-world=empty", \  
"-autoinit"]

