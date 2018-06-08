FROM python:2.7  
# Set environment variables that can be overwritten  
ENV AUTH_SERVICE "ptc"  
ENV USERNAME "username"  
ENV PASSWORD "password"  
ENV LOCATION "Brisbane, Queensland, Australia"  
ENV GOOGLE_MAPS_KEY "google-maps-key"  
ENV TASKS
'[{"type":"HandleSoftBan"},{"type":"CollectLevelUpReward"},{"type":"IncubateEggs","config":{"longer_eggs_first":true}},{"type":"TransferPokemon"},{"type":"EvolvePokemon","config":{"evolve_all":"none","first_evolve_by":"cp","evolve_above_cp":500,"evolve_above_iv":0.8,"logic":"or","evolve_speed":20,"use_lucky_egg":false}},{"type":"RecycleItems","config":{"item_filter":{"Pokeball":{"keep":100},"Potion":{"keep":10},"Super
Potion":{"keep":20},"Hyper Potion":{"keep":30},"Revive":{"keep":30},"Razz
Berry":{"keep":100}}}},{"type":"CatchVisiblePokemon"},{"type":"CatchLuredPokemon"},{"type":"SpinFort"},{"type":"MoveToFort","config":{"lure_attraction":true,"lure_max_distance":2000}},{"type":"FollowSpiral","config":{"diameter":4,"step_size":70}}]'  
ENV FORTS '{"avoid_circles": false,"max_circle_size": 10}'  
ENV WEBSOCKET_SERVER false  
ENV WALK 6  
ENV ACTION_WAIT_MIN 1  
ENV ACTION_WAIT_MAX 4  
ENV DEBUG false  
ENV TEST false  
ENV HEALTH_RECORD true  
ENV LOCATION_CACHE true  
ENV DISTANCE_UNIT "km"  
ENV RECONNECTING_TIMEOUT 15  
ENV EVOLVE_CAPTURED false  
ENV CATCH_RANDOMIZE_RETICLE_FACTOR 1.0  
ENV CATCH_RANDOMIZE_SPIN_FACTOR 1.0  
ENV CATCH '{"any": {"catch_above_cp": 0, "catch_above_iv": 0, "logic": "or"}}'  
ENV RELEASE '{"any": {"keep_best_cp": 3}}'  
ENV VIPS
'{"any":{"catch_above_cp":1200,"catch_above_iv":0.9,"logic":"or"},"Lapras":{},"Moltres":{},"Zapdos":{},"Articuno":{},"Mewtwo":{},"Dragonite":{},"Snorlax":{},"Mew":{},"Arcanine":{},"Vaporeon":{},"Gyarados":{},"Exeggutor":{},"Muk":{},"Weezing":{},"Flareon":{}}'  
  
RUN mkdir /usr/src/app  
  
ARG timezone=Etc/UTC  
RUN echo $timezone > /etc/timezone \  
&& ln -sfn /usr/share/zoneinfo/$timezone /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
RUN apt-get update \  
&& apt-get install -y python-protobuf  
RUN cd /tmp && wget "http://pgoapi.com/pgoencrypt.tar.gz" \  
&& tar zxvf pgoencrypt.tar.gz \  
&& cd pgoencrypt/src \  
&& make \  
&& cp libencrypt.so /usr/src/encrypt.so \  
&& cd /tmp \  
&& rm -rf /tmp/pgoencrypt*  
  
# Working directory for the application  
WORKDIR /usr/src/app  
  
# Clone app into workdir  
RUN git clone -b master https://github.com/PokemonGoF/PokemonGo-Bot .  
  
RUN mv /usr/src/encrypt.so /usr/src/app  
RUN ls /usr/src/app  
ENV LD_LIBRARY_PATH /usr/src/app  
  
# Install all prerequisites (build base used for gcc of some python modules)  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Add start file  
ADD start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
  
# Start  
CMD ["sh", "/usr/local/bin/start.sh"]

