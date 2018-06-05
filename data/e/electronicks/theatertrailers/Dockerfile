FROM alpine:latest  
  
RUN apk add --update \  
python \  
py-pip \  
git \  
&& pip install --upgrade youtube_dl \  
&& pip install tmdbsimple  
  
WORKDIR /  
RUN git clone https://github.com/Electronickss/TheaterTrailers  
RUN mkdir /TheaterTrailers/Logs  
RUN mkdir /TheaterTrailers/Configs  
RUN mkdir /TheaterTrailers/Trailers  
RUN mkdir /TheaterTrailers/Cache  
  
VOLUME ["/TheaterTrailers/Trailers/"]  
VOLUME ["/TheaterTrailers/Logs/"  
VOLUME ["/TheaterTrailers/Configs/"]  
VOLUME ["/TheaterTrailers/Cache/"]  
  
WORKDIR /TheaterTrailers/  
RUN echo "00 */6 * * * /opt/TheaterTrailers/theaterTrailers.py 2 >>
/TheaterTrailers/Logs/theaterTrailers.cron.log" >> mycron && crontab mycron &&
rm mycron  

