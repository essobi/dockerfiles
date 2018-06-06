FROM parity/parity:v1.10.6  
  
RUN ln -s /parity/parity /usr/local/bin/parity  
  
ENTRYPOINT /parity/parity \--jsonrpc-port 8545 \--jsonrpc-interface all
\--jsonrpc-hosts all \--jsonrpc-cors '*' \--ws-interface 0.0.0.0 \--ws-port
8546 \--ws-origins '*' \--ws-hosts all \--cache-size 1024 \--ui-interface
"0.0.0.0" \--ui-hosts all \--ui-no-validation \---force-ui

