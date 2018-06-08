FROM timonier/aria2:1.18.10  
VOLUME /data  
  
ENTRYPOINT [ "/usr/bin/aria2c", "--dir=/data", "--enable-dht", "--dht-listen-
port=6881", "--bt-force-encryption=true", "--bt-require-crypto=true", "--
enable-peer-exchange=true", "--follow-torrent=mem", "--seed-ratio=0.0", "--
check-certificate=false", "--check-integrity=true", "--summary-interval=600",
"--show-console-readout=false"]

