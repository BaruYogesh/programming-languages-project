import System.IO
import Data.String
  
main = do  
    handle <- openFile "../javascript/data.txt" ReadMode  
    contents <- hGetContents handle  

    leaderboardLines <- lines (contents)
    putStr leaderboardLines
    hClose handle  