import System.IO
import Data.String
import Data.List (sortBy)
import Data.Ord (comparing)
import Control.Monad (forM_)
  
main :: IO ()
main = do  
    --handle <- openFile "../javascript/data.txt" ReadMode  
    putStrLn "LEADERBOARD"
    strdata <- readFile "../javascript/data.txt"
    tupleData <- map ((\[s, n] -> (s, read n :: Int)) . words) . lines <$> readFile "../javascript/data.txt"
    --let a = fst(tupleData!!0)
    --putStrLn a
    let sortedData = sortBy sortGT tupleData
    --let b = fst(sortedData!!0)

    printTuples sortedData


    --putStrLn "done"
    
    --hClose handle  
sortGT :: (Ord a1, Ord a2) => (a1, a2) -> (a1, a2) -> Ordering
sortGT (a1, b1) (a2, b2)
  | b1 < b2 = GT
  | b1 > b2 = LT
  | b1 == b2 = compare a1 a2

printTuples :: Show a => [(String, a)] -> IO ()
printTuples xs = forM_ xs (putStrLn . formatOne)

--writeTuplesToFile :: Show a => [(String, a)] -> IO ()
--writeTuplesToFile=
    --writeFile ".../haskell/leaderboard.txt" a
    --xs = forM_xs (writeFile "...haskell/leaderboard.txt" . formatOne)



formatOne :: Show a => (String, a) -> String
formatOne (s,i) = s ++ ": " ++ show i ++ " points"