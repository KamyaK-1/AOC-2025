containedInRanges :: Int -> [(Int,Int)] -> Int
containedInRanges val [] = 0
containedInRanges val ((l,r):xs)
    | (val >= l && val <= r) = 1 
    | otherwise = containedInRanges val xs

main = do
    content <- readFile "input.txt"
    let inp = lines content
    let (rangeInp, rest) = span (/="") inp
        valueInp = drop 1 rest
    let ranges = [ (read a :: Int, read b' :: Int) | line <- rangeInp ,  let (a,b) = span (/='-') line, let b' = tail b  ]
    let values = map read valueInp :: [Int]

    print (sum [(containedInRanges v ranges) | v <- values])
    
