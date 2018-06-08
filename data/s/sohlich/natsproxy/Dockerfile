FROM scratch  
ADD natsproxy-standalone natsproxy-standalone  
  
# Proxy port for HTTP  
ENV PORT 80  
  
# NATS ports  
ENV NATSHOST localhost  
ENV NATSPORT 4222  
EXPOSE $PORT  
CMD ["./natsproxy-standalone"]

