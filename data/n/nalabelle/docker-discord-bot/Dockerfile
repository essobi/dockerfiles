FROM lsiobase/alpine.python3  
  
# set python to use utf-8 rather than ascii.  
ENV PYTHONIOENCODING="UTF-8"  
  
ENV GOOGLE_API_KEY=""  
ENV FORECAST_API_KEY=""  
ENV DISCORD_TOKEN=""  
  
# install app  
RUN \  
echo "**** install pip packages ****" && \  
pip install --no-cache-dir -U \  
discord \  
geocoder \  
giphypop \  
python-forecastio && \  
echo "**** install app ****" && \  
git clone --depth 1 https://github.com/nalabelle/discord-bot.git /app/discord-
bot && \  
echo "**** cleanup ****" && \  
rm -rf \  
/root/.cache \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
WORKDIR /app/discord-bot  

