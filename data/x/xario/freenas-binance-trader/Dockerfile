FROM xario/binance-trader:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="0.2" \  
org.freenas.upgradeable="true" \  
org.freenas.autostart="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/db\", \  
\"descr\": \"sqlite db folder for the orders\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"BINANCE_API_KEY\", \  
\"descr\": \"Binance api key\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"BINANCE_API_SECRET\", \  
\"descr\": \"Binance api secret\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"SYMBOL\", \  
\"descr\": \"Market Symbol (Ex: XVGBTC - XVGETH)\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"QUANTITY\", \  
\"descr\": \"Buy/Sell Quantity\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"AMOUNT\", \  
\"descr\": \"Buy/Sell BTC Amount (Ex: 0.002 BTC)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PROFIT\", \  
\"descr\": \"Target Profit\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAX_AMOUNT\", \  
\"descr\": \"Buy/Sell with max BTC amount True/False\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"STOP_LOSS\", \  
\"descr\": \"Target Stop-Loss % (If the price drops by 6%, sell
market_price.)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"INCREASING\", \  
\"descr\": \"Buy Price +Increasing (0.00000001)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DECREASING\", \  
\"descr\": \"Sell Price -Decreasing (0.00000001)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"WAIT_TIME\", \  
\"descr\": \"Wait Time (seconds)(Ex. 0.7)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"TEST_MODE\", \  
\"descr\": \"Test Mode True/False\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PRINTS\", \  
\"descr\": \"Scanning Profit Screen Print True/False\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DEBUG\", \  
\"descr\": \"Debug True/False\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LOOP\", \  
\"descr\": \"Loop (0 unlimited)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MODE\", \  
\"descr\": \"Working Mode (profit/range)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"BUYPRICE\", \  
\"descr\": \"[Range mode] Buy Price (Price is greater than equal <=)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"SELLPRICE\", \  
\"descr\": \"[Range mode] Sell Price (Price is small than equal >=)\", \  
\"optional\": true \  
} \  
]"  

