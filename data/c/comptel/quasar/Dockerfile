FROM openjdk:8-jre  
  
WORKDIR /home/quasar  
  
COPY entrypoint.sh ./  
  
RUN wget https://github.com/quasar-
analytics/quasar/releases/download/v11.3.6-quasar-web/quasar-
web_2.11-11.3.6-one-jar.jar && \  
chmod +x entrypoint.sh && \  
apt-get update && apt-get install -y --no-install-recommends \  
jq && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 20223  
ENTRYPOINT ["/home/quasar/entrypoint.sh"]  
  
CMD ["java", "-jar", "quasar-web_2.11-11.3.6-one-jar.jar", "-c", "quasar-
config.json"]  

