import Data.List (sort)


getLength :: (Int,Int) -> [(Int,Int)] -> Int
getLength (end,length) [] = length
getLength (end,length) ((interval_start, interval_end):xs)
    | (end < interval_start) = getLength (interval_end, 1 + interval_end - interval_start + length) xs
    | (end >= interval_end)  = getLength (end, length) xs
    | otherwise              = getLength (interval_end, length + interval_end - end) xs

main = do
    content <- readFile "input.txt"
    let inp = lines content
    let (rangeInp, rest) = span (/="") inp
        valueInp = drop 1 rest
    let ranges = [ (read a :: Int, read b' :: Int) | line <- rangeInp ,  let (a,b) = span (/='-') line, let b' = tail b  ]
    let sortedRanges = sort ranges
    print  (getLength (0,0) sortedRanges)
    
