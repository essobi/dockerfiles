FROM alpine:latest  
  
RUN apk add --update \  
tar \  
python \  
python-dev \  
py-pip \  
curl \  
build-base \  
gcc  
  
RUN mkdir /app && cd /app \  
&& curl -SLs -O https://github.com/AHAAAAAAA/PokemonGo-
Map/archive/master.tar.gz \  
&& tar -xzv --strip-components=1 -f master.tar.gz \  
&& rm master.tar.gz \  
&& pip install -r requirements.txt  
  
ADD 0001-Adding-override-for-Google-Maps-API-key.patch /  
RUN cd app && patch -p1 < /0001-Adding-override-for-Google-Maps-API-key.patch  
  
ENV USERNAME=""  
ENV PASSWORD=""  
ENV LOCATION="42.3381440 -71.0475770"  
ENV GOOGLE_API=""  
ADD start.sh /start.sh  
RUN chmod a+x /start.sh  
  
WORKDIR /app  
EXPOSE 5000  
ENTRYPOINT ["/start.sh"]

