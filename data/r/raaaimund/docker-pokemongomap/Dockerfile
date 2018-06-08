# Dockerizing PokemonGo-Map: Dockerfile for building PokemonGo Map  
# Based on ubuntu:latest, installs PokemonGo-Map following the instructions
from:  
# https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Installation-and-
requirements  
# docker run -d --name pokemap -e pokemon_Username=USRENAME -e
pokemon_Location=47.33,16.44 -e pokemon_Password=PASSWORD -e
pokemon_AuthType=PTC_OR_GOOGLE -e pokemon_StepLimit=10 -e
pokemon_Gmapskey=GOOGLE_MAPS_KEY -p 8080:5000 raaaimund/docker-pokemongomap  
FROM ubuntu:latest  
  
MAINTAINER raaaimund raimund@rittnauer.at  
  
# Install Ubuntu Upgrades and required Software  
RUN apt-get update && apt-get install -y \  
git \  
python \  
python-pip  
  
# Upgrade Python Installer PIP  
RUN pip install --upgrade pip  
  
# Clone Develop Branche of PokemonGo-Map from Github  
RUN git clone https://github.com/AHAAAAAAA/PokemonGo-Map -b develop
/home/PokemonGo-Map  
  
# Install PokemanGo-Map Requirements  
RUN pip install --upgrade -r /home/PokemonGo-Map/requirements.txt  
  
# This command is run while Starting Docker Container  
CMD cd /home/PokemonGo-Map && python /home/PokemonGo-Map/runserver.py \  
-a $pokemon_AuthType \  
-u $pokemon_Username \  
-p $pokemon_Password \  
-l $pokemon_Location \  
-st $pokemon_StepLimit \  
-k $pokemon_Gmapskey \  
-H 0.0.0.0  
  

