FROM poad/docker-jupyter-haskell-base:latest  
  
LABEL Kenji Saito "ken-yo@mbr.nifty.com"  
  
RUN ihaskell install --stack && \  
rm -rf /tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8888  
WORKDIR /root/IHaskell  
  
CMD ["stack", "exec", "--", "jupyter", "notebook", "--port=8888", "--ip='*'",
"--no-browser", "--allow-root"]  

