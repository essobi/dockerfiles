FROM haskell  
  
RUN \  
cabal update && \  
cabal install hoogle && \  
hoogle generate && \  
echo ':def hoogle \x -> return $ ":!hoogle \"" ++ x ++ "\""' >> /root/.ghci &&
\  
echo ':def doc \x -> return $ ":!hoogle --info \"" ++ x ++ "\""' >>
/root/.ghci && \  
rm -r /root/.cabal/packages  
  

