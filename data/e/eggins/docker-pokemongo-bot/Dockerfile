FROM python:2.7-alpine  
  
# Set environment variables that can be overwritten  
ENV AUTH_SERVICE "google" \  
USERNAME "username" \  
PASSWORD "password" \  
LOCATION "LAT LON" \  
GOOGLE_MAPS_KEY "google-maps-api-key" \  
MAX_STEPS "5" \  
MODE "all" \  
WALK "4.16" \  
DEBUG "false" \  
TEST "false" \  
INITIAL_TRANSFER 0 \  
LOCATION_CACHE "true" \  
DISTANCE_UNIT "km" \  
ITEM_FILTER "101,102,103,104" \  
EVOLVE_ALL "NONE"  
# Working directory for the application  
WORKDIR /usr/src/app  
  
# add certificates to talk to the internets  
RUN apk add --no-cache ca-certificates git nano  
  
# Clone app into workdir  
RUN git clone https://github.com/PokemonGoF/PokemonGo-Bot .  
  
# Install all prerequisites (build base used for gcc of some python modules)  
RUN apk add --no-cache build-base \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apk del build-base  
  
# Default port the webserver runs on  
EXPOSE 5000  
CMD python pokecli.py \  
-a $AUTH_SERVICE \  
-u $USERNAME \  
-p $PASSWORD \  
-l $LOCATION \  
-lc $LOCATION_CACHE \  
-m $MODE \  
-w $WALK \  
-k $GOOGLE_MAPS_KEY \  
-ms $MAX_STEPS \  
-it INITIAL_TRANSFER \  
-d $DEBUG \  
-du $DISTANCE_UNIT \  
-if $ITEM_FILTER \  
-ev $EVOLVE_ALL \  
&& cd web && python -m SimpleHTTPServer -p 5000

