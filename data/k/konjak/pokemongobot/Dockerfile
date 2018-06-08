FROM anapsix/alpine-java:latest  
MAINTAINER Konstantin Jakobi <konstantin@jakobi.club>  
RUN apk add --no-cache git wget grep coreutils  
WORKDIR /PokemonGoBot  
RUN VERSION=$(git ls-remote --tags https://github.com/jabbink/PokemonGoBot |
grep -Po '[0-9]\\.[0-9]\\.[0-9]' | sort -V | tail -n 1) \  
&& wget -O /PokemonGoBot/config.properties
https://raw.githubusercontent.com/jabbink/PokemonGoBot/master/config.properties.template
\  
&& wget -O /PokemonGoBot/pogo.scraper-all.jar
https://github.com/jabbink/PokemonGoBot/releases/download/v${VERSION}/PokemonGoBot-${VERSION}.jar  
COPY run.sh /PokemonGoBot/  
CMD ["./run.sh"]  

