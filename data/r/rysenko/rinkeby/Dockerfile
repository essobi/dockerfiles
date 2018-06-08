FROM ethereum/client-go:stable  
EXPOSE 8545  
EXPOSE 30303  
ENTRYPOINT ["geth", "--rinkeby", "--fast", "--cache", "2048", "--rpc", "--
rpcaddr", "0.0.0.0", "--rpccorsdomain" , "*", "--rpcapi",
"eth,net,web3,personal,debug"]  

